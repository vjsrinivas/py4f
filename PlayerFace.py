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


#EXTREME BETA
class Limiter:

    def __init__(self):
        self.profile = Profiling("en")
        self.tempoffenders = []

    def _detectiveLoadout(self, args, source, type, cmd):
        internal = []
        for i in range(0, len(source)):
            internal.append(self.profile.getloadout(source[i].nucleus, source[i].profile))
            barrer = len(internal[i]["data"]["equipment"])
            keeper = 0
            while keeper < barrer:
                for e in range(len(args)):
                    if internal[i]["data"]["equipment"][keeper][type] == args[e]:
                        if keeper + 1 == barrer:
                            self.evoker(source[i].playername)
                        else:
                            continue
                    else:
                        continue
                keeper += 1
        return

    def evoker(self, inputer):
        #Adding to repeat offenders list
        self.tempoffenders.append(inputer)
        #check if duplicate of same name (i.e. repeat offender)
        hasseen = set()
        for i in self.tempoffenders:
            if i in hasseen:
                print("Repeat Offender!")
            else:
                continue
        #smthsmth action...
        return
