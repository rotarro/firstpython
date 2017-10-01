import tweepy

def crawling_twitter_mention() :

	consumer_key = 'G9JzFD2FymO3h5dpvG52zKe5H'
	consumer_secret = 'CyRqDLpi2fW7ttCsfGBusLH5oJdXlaRBD4zUpFr2v010nMnTEN'

	access_token = '208308487-ezP0oQxgDPc36btkQkDoAN1hWOBUi8HYEElTn5ES'
	access_token_secret = 'uqXgze2pfJQVIOEMnxcTZNKzlT2Yt1GQWARSu6SJUOqP4'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	search_keyword = '무뚝뚝감자칩'

	tweets = api.search(search_keyword)

	return tweets

