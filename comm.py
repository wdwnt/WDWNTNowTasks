import tweepy

class Comm(object):
	
	@staticmethod
	def tweet(msg, cfg):
		auth = tweepy.OAuthHandler(cfg['TWITTER_CONSUMER_KEY'], cfg['TWITTER_CONSUMER_SECRET'])
		auth.set_access_token(cfg['TWITTER_ACCESS_KEY'], cfg['TWITTER_ACCESS_SECRET'])
		twitter_api = tweepy.API(auth)
		print 'Sending tweet...'
		twitter_api.update_status(status=msg)