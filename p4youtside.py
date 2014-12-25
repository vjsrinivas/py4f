__author__ = 'Vijaysrinivas Rajagopal'

import urllib.request, urllib.error, json


class GrabSource:
    """
    Grabs needed files (usually in JSON format) for processing and compiling during runtime
    """
    def __init__(self):
        self.rawdata = ""
        self.jsondata = None

    def sourcegrab(self, url):
        """
        Retrieves data from a source and stores it in self.rawdata as a string for later parsing by jsonparse()
        :param url: Used to direct http.client for retrieval
        :return complete data or -1 (Error):
        """
        try:
            c = urllib.request.urlopen(url)
            return c.read()
        except (urllib.error.HTTPError, urllib.error.URLError, urllib.error.URLError, Exception) as e:
            print(e)
            return -1

    def jsonparse(self, stringer = None):
        """
        Parses string data from self.rawdata into an array in self.jsondata.
        Call self.jsondata just like you would with a normal array
        :return Nothing:
        """
        try:
            self.jsondata = json.loads(self.rawdata)
            #debug print(json.dumps(self.jsondata, sort_keys = true, indent=4)
            #debug print(self.jsondata['mapname'])
        except(TypeError, KeyError, ValueError, Exception) as e:
            print(e)

    def sourceoffline(self, filename, moder="r"):
        """
        NOT RECOMMENDED FOR USE.
        In case the URL of the source file does not work, this is a fallback [JSON created 9/25/14]
        :param filename:
        :param moder:
        :return:
        """
        try:
            file = open(filename, mode = moder, buffering=1)
            self.rawdata = file.read()
            self.jsonparse()
        except Exception as e:
            print(e)
        return