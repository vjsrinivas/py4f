__author__ = 'Vijaysrinivas Rajagopal'

from p4youtside import *


#racial, religious, and more! Brought to you by the letter T, S, and A!
class Profiling:
    """
    Used for grabbing extraneous player information from Player Profile Pages for later use.
    IMPORTANT NOTES:
        > For typeparam:
            - [%22GameEventStats%22]
            - [%22CoreStats%22]
            - [%22BadPlayerStats%22]
            - [%22GameModeStats%22]
            - [%22VehicleStats%22]
            - [%22MapStats%22]
            - [%22GameModeMapStats%22]
            - [%22RushMapStats%22]
        > You can combine all these parameters for as much content you need
        > Call getcomplete returns a list containing profile/stats [0] and profile/loadout [1]
    """
    def __init__(self, LANGUAGE="en"):
        self.language = LANGUAGE
        self.urlarchor = "http://battlefield.play4free.com/{}/profile/".format(self.language)

    def getprofinfo(self, nucleusnum, profilenum, typeparam):
        urler = self.urlarchor + "stats/" + nucleusnum + "/" + profilenum + "?g=" + typeparam
        grabber = GrabSource()
        grabber.rawdata = grabber.sourcegrab(urler).decode("utf-8")
        grabber.jsonparse()
        return grabber.jsondata

    def getloadout(self, nucleusnum, profilenum):
        urler = self.urlarchor + "loadout/" + nucleusnum + "/" + profilenum
        grabber = GrabSource()
        grabber.rawdata = grabber.sourcegrab(urler).decode("utf-8")
        grabber.jsonparse()
        return grabber.jsondata

    def getcomplete(self, nucleusnum, profilenum, typeparam):
        import json
        urler = self.urlarchor + "stats/" + nucleusnum + "/" + profilenum + "?g=" + typeparam
        urler2 = self.urlarchor + "loadout/" + nucleusnum + "/" + profilenum
        grabber = GrabSource()
        internalraw1 = grabber.sourcegrab(urler).decode("utf-8")
        internalraw2 = grabber.sourcegrab(urler2).decode("utf-8")
        internalraw1 = json.loads(internalraw1)
        internalraw2 = json.loads(internalraw2)
        return [internalraw1, internalraw2]

    """def supply(self, source):
        for i in range(0, len(source)):
            self.getcomplete(source[i].nucleus, source[i].profile, "[%22CoreStats%22, %%22, %22%22]")"""


#EXTREME BETA
class Limiter:

    def __init__(self):
        return

    def _detective(self, args, source):
        for i in range(len(source)):
            return
        return

profile = Profiling("en")
profile.getprofinfo("2812236316", "817448226", "[%22CoreStats%22,%22BadPlayerStats%22]")
jsonholder = profile.getcomplete("2812236316", "817448226", "[%22CoreStats%22,%22BadPlayerStats%22]")
print(jsonholder[1]["data"]['equipment'][0])