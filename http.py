import config
import json
import requests

class Http(object):

    @staticmethod
    def get(url, no_print=False):
        url = config.HOST_URL + url
        if not no_print:
            print "GET " + url
            print "..."
        return requests.get(url)