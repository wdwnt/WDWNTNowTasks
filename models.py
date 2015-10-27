import json
from datetime import datetime
from util import Util
from http import Http

class Attraction(object):
	@staticmethod
	def get(args):
		r = Http.get("/attraction/get/" + args[2], True)
		return "{} {} minutes".format(args[1], r.json()['PostedWaitTime'])