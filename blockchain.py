

import time
import hashlib


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash(data)

    def __repr__(self):
        return 'Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)

    @staticmethod
    def _calc_hash(string: str) -> str:
        """
        Given a string, calculates the SHA-256 hash of it
        :param string: text we want to calculate th hash of
        :return: hash of the imputed text
        """
        sha = hashlib.sha256()
        sha.update(string.encode('utf-8'))
        return sha.hexdigest()


class BlockChain(object):
    def __init__(self):
        self.tail = None

    def append(self, data):
        """ Append a value to the end of the BlockChain. """

        if self.tail is None:
            self.tail = Block(data=data, previous_hash=None)

        else:
            self.tail = Block(data=data, previous_hash=self.tail)

    def search(self, data):
        """ Search the BlockChain for a node with the requested value and return the node. """

        if self.tail is None:
            print(" 'append' data on the BlockChain before searching for it")
            return

        else:
            position_head = self.tail

            while position_head.previous_hash:  # Moving to the start of the BlockChain
                if position_head.data == data:
                    return position_head
                position_head = position_head.previous_hash

            return None

    def size(self):
        """ Return the size or length of the BlockChain. """
        position_head = self.tail
        length = 0

        while position_head is not None:
            position_head = position_head.previous_hash
            length += 1

        return length

    def to_list(self):
        """Transforms the BlockChain content into a list"""
        out = []
        block = self.tail
        while block:
            out.append([block.data, block.timestamp, block.hash])
            block = block.previous_hash
        return out


#################################

blockchain = BlockChain()

print(blockchain.size())

##################### 0


print(blockchain.to_list())

###################### []

blockchain.append('my balance: 0 | cash flow: +10 | final balance: 10')

print(blockchain.size())

########################## 1

print(blockchain.to_list())

###################################
blockchain.append('my balance: 10 | cash flow: +25 | final balance: 35')
blockchain.append('my balance: 35 | cash flow: -15 | final balance: 20')
blockchain.append('my balance: 20 | cash flow: +125 | final balance: 145')
blockchain.append('my balance: 145 | cash flow: +5 | final balance: 150')
print(blockchain.size())
################################## 5
print(blockchain.to_list())
########################################

#############################"search function"

print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))



######################## Edge :

print(blockchain.search('my balance: 1000 | cash flow: +100 | final balance: 1100'))

####################### None

blockchain = BlockChain()

print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))

############################
