from comm import Comm
from http import Http

class Attraction(object):
	@staticmethod
	def get(attraction):
		url = "{}{}".format("/attraction/get/", attraction['id'])
		res = Http.get(url, True)
		json = res.json()
		
		status = ''
		
		if json['ShortWaitTimeDisplay'] == 'Closed':
			status = attraction['closed_message']
		else:
			status = "{} {} minutes".format(attraction['open_message'], json['PostedWaitTime'])
			
		if 'twitter_cfg' in attraction:
			Comm.tweet(status, attraction['twitter_cfg'])
		else:
			print status