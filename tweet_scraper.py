from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
import csv
import re

#set date according to your preference
#the tweets will be scraped a day prior than the end_date
begin_date = dt.date(2020,7,26)
end_date = dt.date.today()

#enter the amount of tweets you want 
#the limit might not be accurate you might get 10-20 more or less tweets
limits = input("Enter number of tweets you want to scrape:\n")
limits = int(limits)

#to get tweets in english
langs = "english"

#to get the tweets
basic_tweets = query_tweets("#news" , begindate=begin_date, enddate=end_date , limit=limits, lang=langs)
user1_tweets = query_tweets("@PolitiFact" , begindate= begin_date, enddate=end_date, limit=limits, lang=langs)
user2_tweets = query_tweets("@GossipCop" , begindate= begin_date, enddate=end_date, limit=limits, lang=langs)

#to store the tweets in csv files using pandas
df = pd.DataFrame(b.__dict__ for b in basic_tweets)
df.drop(df.columns.difference(['username','text']), 1, inplace=True)
df.to_csv("C:/fake_news_detection/csv_files/tweet.csv", index= False)

df1 = pd.DataFrame(u1.__dict__ for u1 in user1_tweets)
df1.drop(df1.columns.difference(['username','text']), 1, inplace=True)
df1.to_csv("C:/fake_news_detection/csv_files/politifact.csv" , index= False)

df2 = pd.DataFrame(u2.__dict__ for u2 in user2_tweets)
df2.drop(df2.columns.difference(['username','text']), 1, inplace=True)
df2.to_csv("C:/fake_news_detection/csv_files/gossipcop.csv" , index= False)