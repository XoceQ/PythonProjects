import tweepy
import time

auth = tweepy.OAuthHandler(' ')# Paste your CONSUMER API KEYS
auth.set_access_token(' ') # #Paste your Access Token and Access Token secret


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Javascript','100DaysOfCode','DEVCommunity' #hashtags
nrTweets = 50 #n number of tweets 

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('retweeted')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break 
