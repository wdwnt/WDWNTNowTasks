from config import Config
import json
import requests

class Http(object):

    @staticmethod
    def get(url, no_print=False):
        url = Config.host() + url
        if not no_print:
            print "GET " + url
            print "..."
        return requests.get(url)