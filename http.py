import json
import requests

class Http(object):

    @staticmethod
    def get(url, headers, no_print=False):
        #url = Config.get("host") + url
        url = "http://now.wdwnt.com" + url
        if not no_print:
            print ("GET " + url)
            print ("...")
        return requests.get(url, headers=headers)