import json
from datetime import datetime
from util import Util
from http import Http

class Attraction(object):
	@staticmethod
	def get(attraction):
		url = "{}{}".format("/attraction/get/", attraction['id'])
		res = Http.get(url, True)
		json = res.json()
		
		if json['ShortWaitTimeDisplay'] == 'Closed':
			return attraction['closed_message']
		else:
			return "{} {} minutes".format(attraction['open_message'], json['PostedWaitTime'])