# feel free to use this code for whatever you want
# it is mostly based on small code snippets that demonstrate the usage of tweepy
# purpose of this script is to read twitter follower ids from a pickled file
# once loaded the script will randomly choose one follower and print out:
# name, profile url, follower count, friends count and statuses count
# WARNING: selected numbers are from 0 to X

import sys
import tweepy
import pickle

import keys
import random

try:
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    
    rnd = random.SystemRandom()
    
    pkl_file = open('follower.pkl', 'rb')

    ids = pickle.load(pkl_file)
    
    page = rnd.randint(0, len(ids)-1)
    entry = rnd.randint(0, len(ids[page])-1)
    
    print "randomly selecting page %u of %u pages" % (page, len(ids))
    print "randomly selecting entry %u of %u entries in page %u" % (entry, len(ids[page]), page)
    
    user = api.get_user(user_id=ids[page][entry])
    print "randomly selected user is: %s" % user.screen_name
    print "URL to this user: https://www.twitter.com/%s" % user.screen_name
    print "Followers: %u" % user.followers_count
    print "Friends: %u" % user.friends_count
    print "Statuses: %u" % user.statuses_count

except tweepy.TweepError:
    print tweepy.TweepError.message
except:
    print sys.exc_info()