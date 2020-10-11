import csv
import tweepy
import ssl
from decouple import config
# Oauth keys

# Twitter Credentials Obtained from http://dev.twitter.com
consumer_key = config('COMSUMER_KEY')
consumer_secret = config('COMSUMER_SECRET')
access_key = config('ACCESS_KEY')
access_secret = config('ACCESS_SECRET')

# Create Auth object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
ssl._create_default_https_context = ssl._create_unverified_context
api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# # Authentication with Twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
# api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.me()
print (user.name)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'realDonaldTrump'
tweet_id = ['1312233807991496704']

replies=[]
bidenReplies = []
try:
    # for t in tweepy.Cursor(api.user_timeline, screen_name=name).pages():
    #     print(t)
    #     break
    # for t in tweepy.Cursor(api.search, q='name', since = "2020-09-20", until = "2020-09-21", timeout=999999).pages():
    #     print(t)
    #     break
    a = 0
    for tweet in tweepy.Cursor(api.search,
                           q="DonaldTrump",
                           count=2000,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items(2000):
        # print(tweet.text)
        replies.append(tweet)
        # if a == 0:
        #     print(tweet)
        #     a = 1
    for tweet in tweepy.Cursor(api.search,
                           q="JoeBiden",
                           count=2000,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items(2000):
        # print(tweet.text)
        bidenReplies.append(tweet)
    # for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(100):
    #     if hasattr(tweet, 'in_reply_to_status_id_str'):
    #         if (tweet.in_reply_to_status_id_str==tweet_id):
    #             replies.append(tweet)
except:
    print(replies)
    traceback.print_exc() 
    

with open('trump_data.csv', 'a+') as f:
    # csv_writer = csv.DictWriter(f, fieldnames=('created_at','user', 'text'))
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in replies:
        # row = {'created_at': tweet.created_at.strftime('%d-%m-%Y %H:%M:%S'), 'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ').replace('\r','')}
        csv_writer.writerow(row)

with open('biden_data.csv', 'a+') as f:
    # csv_writer = csv.DictWriter(f, fieldnames=('created_at','user', 'text'))
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in bidenReplies:
        # row = {'created_at': tweet.created_at.strftime('%d-%m-%Y %H:%M:%S'), 'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ').replace('\r','')}
        csv_writer.writerow(row)
