from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
import csv
import re

#set date according to your preference
#the tweets will be scraped a day prior than the end_date
begin_date = dt.date(2020,7,25)
end_date = dt.date.today()

#enter the amount of tweets you want 
#the limit might not be accurate you might get 10-20 more or less tweets
limits = input("Enter number of tweets you want to scrape:\n")
limits = int(limits)

#to get tweets in english
langs = "english"

user1 = "PolitiFact"
user2 = "GossipCop"

#to get the tweets
basic_tweets = query_tweets("#news" , begindate=begin_date, enddate=end_date , limit=limits, lang=langs)
user1_tweets = query_tweets(user1 , begindate= begin_date, enddate=end_date, limit=limits, lang=langs)
user2_tweets = query_tweets(user2 , begindate= begin_date, enddate=end_date, limit=limits, lang=langs)

#to store the tweets in csv files using pandas
df = pd.DataFrame(b.__dict__ for b in basic_tweets)
df.drop(df.columns.difference(['username','text']), 1, inplace=True)
#to get only username and text of a tweet
df.to_csv("C:/tweet_scraper/tweets/tweet.csv", index= False)

df1 = pd.DataFrame(u1.__dict__ for u1 in user1_tweets)
#to get everything from the tweet i.e 
# username, text, retweet, time, likes,etc
df1.to_csv("C:/tweet_scraper/tweets/politifact.csv" , index= False)

df2 = pd.DataFrame(u2.__dict__ for u2 in user2_tweets)
#you can also store the data in json format just by replacing csv by json
#but first you need to create a file named xyz.csv/xyz.json
df2.to_csv("C:/tweet_scraper/tweets/gossipcop.csv" , index= False)