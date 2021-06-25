# Save the frogs Twitter bot requested by @saiboguninja

import tweepy, requests, json

# Authenticate to Twitter
# this is where you insert your keys from your Twitter developer account
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("YOU WILL LIVE ON A FARM.\n YOU WILL EAT ORGANIC FOOD.\n YOU WILL HAVE A LOVING WIFE.\n YOU WILL HAVE CHILDREN.\n YOU WILL DEFEAT THE GLOBALISTS.\n YOU WILL SAVE THE FROGS.")