import tweepy

def login(acount):
  if acount =="TwitterAPIアカウントid":

      # The consumer keys can be found on your application's Details
      # page located at https://dev.twitter.com/apps (under "OAuth settings")
      consumer_key=""
      consumer_secret=""

      # The access tokens can be found on your applications's Details
      # page located at https://dev.twitter.com/apps (located
      # under "Your access token")
      access_token=""
      access_token_secret=""


      auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
      auth.set_access_token(access_token, access_token_secret)

      api = tweepy.API(auth)
      return api
  else:
    exit()
