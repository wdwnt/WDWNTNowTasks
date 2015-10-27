import json
import collections
import urllib

class Util(object):

    @staticmethod
    def print_json(response):
        try:
            print "{} {}".format(response.status_code, response.reason)
            print json.dumps(json.loads(response.text), indent=2)
        except ValueError as e:
            print str(e)

    @staticmethod
    def print_response(response):
        print "{} {}".format(response.status_code, response.reason)

    @staticmethod
    def parse_args(args):
        params = dict()
        for arg in args:
            if "=" in arg:
                params[arg.split("=")[0]] = arg.split("=")[1]

        return params

    @staticmethod
    def urlencoded_querystring(params):
        ordered_params = collections.OrderedDict(sorted(params.items()))
        return urllib.urlencode(ordered_params)

    @staticmethod
    def urldecode(querystring):
        return urllib.unquote(querystring).decode("utf8")