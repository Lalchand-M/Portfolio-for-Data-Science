import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.data).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return ('Timestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}'.format(self.timestamp, self.data, self.previous_hash, self.hash))

class Blockchain:

    def __init__(self):
        self.current_block = None

    def add_block(self, value):
        timestamp = time.gmtime()
        data = value
        previous_hash = self.current_block.hash if self.current_block else 0
        self.current_block = Block(timestamp, data, previous_hash)
# Test#
blockchain = Blockchain()


print(blockchain.size())
# 0
print(blockchain.to_list())
# []

blockchain.append('my balance: 0 | cash flow: +10 | final balance: 10')
print(blockchain.size())
# 1
print(blockchain.to_list())
# 
# 

blockchain.append('my balance: 10 | cash flow: +25 | final balance: 35')
blockchain.append('my balance: 35 | cash flow: -15 | final balance: 20')
blockchain.append('my balance: 20 | cash flow: +125 | final balance: 145')
blockchain.append('my balance: 145 | cash flow: +5 | final balance: 150')
print(blockchain.size())
# 5
print(blockchain.to_list())
#

# Test "search function"
print(blockchain.search('my balance: 145 | cash flow: +5 | final balance: 150'))
# 

# Edge Case:
print(blockchain.search('my balance: 1000 | cash flow: +100 | final balance: 1100'))
# 

blockchain = BlockChain()
print(blockchain.search('my balance: 145 | cash flow: +5 | final balance: 150'))
# 
blockchain = BlockChain()

blockchain.add_block(1)
print(blockchain.current_block)

blockchain.add_block(2)
print(blockchain.current_block)

blockchain.add_block(3)
print(blockchain.current_block)
