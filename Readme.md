# Tweet scraper

## Using twitterscraper

Twitter's API is very hard to work with, and has lots of limitations — luckily this library solves that problem. No API rate limits. No restrictions. Extremely fast

No developers account or any sort of twitter account required to scrape tweets

You can scrape tweets of any Twitter user or any hashtags

![Alt text](https://img.shields.io/badge/python-v3.8-g)
![Alt text](https://img.shields.io/badge/twitterscraper-v1.4.0-yellow)

# Pre-Requisite

- Python v3.8
- twitterscraper library

# Installing twitterscraper

If you want to use latest version, install from source. To install twitter-scraper from source, follow these steps:

Linux and macOS:

    git clone https://github.com/taspinar/twitterscraper.git
    cd twitter-scraper
    sudo python3 setup.py install 
Also, you can install with PyPI.

    pip install twitterscraper

# Output

### Per Tweet it scrapes the following information:

- Tweet_id
- Tweet_url
- Tweet text
- Tweet html
- Links inside Tweet
- Hashtags inside Tweet
- Image URLS inside Tweet
- Video URL inside Tweet
- Tweet timestamp
- Tweet Epoch timestamp
- Tweet No. of likes
- Tweet No. of replies
- Tweet No. of retweets
- Username
- User Full Name / Screen Name
- User ID
- Tweet is an reply to
- Tweet is replied to
- List of users Tweet is an reply to
- Tweet ID of parent tweet

### In addition it can scrape for the following user information:

- Date user joined
- User location (if filled in)
- User blog (if filled in)
- User No. of tweets
- User No. of following
- User No. of followers
- User No. of likes
- User No. of lists
- User is verified

## Output files:

All of the retrieved Tweets are stored in the indicated output file that maybe csv, json or anyother file type.

The output files can be stored and opened using pandas dataframe

    import pandas as pd
    df = pd.DataFrame(b.__dict__ for b in tweets)


