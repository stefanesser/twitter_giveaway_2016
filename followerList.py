# feel free to use this code for whatever you want
# it is mostly based on small code snippets that demonstrate the usage of tweepy
# purpose of this script is to enumerate all follower ids of 'i0n1c' and
# then pickle them into a file
# WARNING: sometimes strange TweepError exceptions are thrown at the very end

import sys
import tweepy
import pickle

import keys

try:
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    
    follower_cursor = tweepy.Cursor(api.followers_ids, id = "i0n1c")
    print "type[follower_cursor]=", type(follower_cursor)
    ids = []
    count = 0
    for p in follower_cursor.pages():
        ids.append(p)
        count += len(p)
        print "At %u" % count
    
    output = open('follower.pkl', 'wb')
    pickle.dump(ids, output, -1)
    output.close()
    
except tweepy.TweepError:
    print tweepy.TweepError.message
except:
    print sys.exc_info()
