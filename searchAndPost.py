import tweepy
from keys import *

# post tweet on account (with text and media)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#update w text
#api.update_status('Hello world')

#update w pic and text (cute dog)
api.update_with_media('1.jpg', "Rating: 4.5")

#update w pic and text (sad dog)
api.update_with_media('2.jpg', "Rating: 2")

#update w pic and text (candy)
#api.update_with_media('3.jpg', "Rating: 5")

#update w pic and text (fur coat)
#api.update_with_media('4.jpg', "Rating: 1.5")