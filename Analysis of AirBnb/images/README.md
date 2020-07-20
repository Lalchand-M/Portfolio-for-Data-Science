# [Project 1: Analysis of Boston and Seattle AirBnb Data](https://lalchand-m.github.io/Portfolio-for-Data-Science/)

# Project Overview:

# About AirBnb:

AirBnb is an online marketplace that connects people who want to rent out their homes with people who are looking for accommodations in that locale. Airbnb takes a unique approach toward lodging. Part of the “sharing economy,” Airbnb offers someone’s home as a place to stay instead of a hotel. Host can rent out extra space in their own home and make some extra money for allowing a guest to stay the night.

# Analysis:

Based on Industry Standard Process of Data Mining, the Boston and Seatle Airbnb datasets were collected and analysed. 

Three bisinuess questions were asked and answered:

* Is there any noticeable difference between Seattle and Boston Airbnb?
* What are the most important features to estimate Airbnb rental price?
* What are the top amenities people needs most?

# DataSets:

Two datasets of AirBnB for Boston and Seattle which were collected from the link  http://insideairbnb.com/get-the-data.html

# Results and analysis:

AirBnb Boston and Seattle dataset were analysed and found some interesting information. These interesting informations are shared below.

* Boston and Seattle Airbnb datasets were collected and compared.
* Machine learning model was established to predict the rental price for both cities.
* Featured importance of the trained model were looked and checked if they make sense.
* List of important amenities were shared as to how host can make more money by providing better services to meet customers need.

# Number Of Listings: 

We understand from the Data Set that Boston has 7,032 listings with an average of $ 200 per night, while Seattle has 9,562 listings with an average of $ 160 per night.

Understanding of price range: 70% of Boston listings are below $ 250 / night, while 70% of Seattle listings are below $ 200 / night, suggesting that the Airbnb rental price in Seattle is Boston. That is, it is a little cheaper than

The most expensive list in Boston is $ 4,000 / night, while the most expensive in Seattle is $ 5,800 / night.
Airbnb hosts can list entire houses / apartments (red), private (green) or shared rooms (blue). In Boston, the hosts listed their room types as 62.2%, 36.6%, and 1.2%, respectively, as in the previous three room types. While the room type in Seattle was 66.6%, 30.4% and 3.1% respectively.

We drilled more deeply at the dataset and estimated the AirBnB rental price in Boston and Seattle.

# Rental Price Forecasts in Boston and Seattle:

The 99% listing price is below 600 and we omit the rows above 600 for a more stable prediction. Missing values ​​were filled with the highest value based on the mean value or other related characteristics.

GradientBoostingRegressor was used as a classifier for both data sets and a GridSearch CV of five times was applied to find the best hyperparameter for the classifier. On the other hand, 1/5 of the preprocessed data set was used as test data and the remaining 4/5 were used to train the learning model.


# Important Features in deciding the Rental Price:

# In Boston:

Latitude and longitude are among the main important features, since the price of a rental largely depends on the location of the property. Host_since is a feature that when hosts start their journey with AirBNB, if there is AirBNB upon starting the host, they probably know that they attract people and make their guests feel more comfortable. Reviews_per_month and number_of_reviews give us information about people who are not only ready to be there, but also leave a comment, which means they enjoy the stay. Some other features like fit, tank_safety and bathroom are also listed above.

![](https://github.com/Lalchand-M/Portfolio-for-Data-Science/blob/master/images/image1.png)
# In Seattle:

Facilities provided by the hosts are looked as an important feature by the travellers. There are some new features like host_response_rate, extra_people and guest_included. But most of the standout features have been shared with the Boston machine learning model. We can see that cleaning_fee is the most important feature here, as larger rooms require more cleaning, perhaps more bathrooms, and more amenities.

![](https://github.com/Lalchand-M/Portfolio-for-Data-Science/blob/master/images/image2.png)

# Features that plays an important role:

Training the machine learning model we can examine how amenities plays an important role in revenue generation. 

* In Boston, facilities like television & Internet are the most important deciding factor. Place which provides a friendly and family environment scores the most.An interesting data is that Seattle tops in amenities as 180 when compared to Boston 125.

![](https://github.com/Lalchand-M/Portfolio-for-Data-Science/blob/master/images/image3.png)

* Seattle boast some extra amenites when compared to Boston, like Amazon Echo, Wooden Floors, Dinning Area, and Memory Foam Mattress. The choise of these amenities are guest dependent therefore hosts provide these facilities as much as they can. First-aid-kit is looked as an Very important add-on in Seattle.

![](https://github.com/Lalchand-M/Portfolio-for-Data-Science/blob/master/images/image4.png)



