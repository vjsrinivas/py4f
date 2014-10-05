__author__ = 'Vijaysrinivas Rajagopal'

from RCONBase import TCPBARE
import ClientFace, time, datetime
from Chatter import*
import datetime


class PlayerStruc:
    __slots__ = ['index', 'playername', 'nucleus', 'profile', 'score', 'ping', 'kills', 'deaths', 'alive', 'game_class',
                 'rank', 'team', 'connected', 'suicides', 'cp_captures', 'cp_defends', 'cp_assists', 'cp_neutralizes',
                 'kit', 'position', 'vehicle_name', 'vehicle_type', 'isAI', 'cp_revives', 'cp_damageassists',
                 'cp_passengerassists', 'cp_targetassists', 'idle']

    def __init__(self):
        self.playername = None
        self.nucleus = None
        self.profile = None
        self.score = None
        self.ping = None
        self.kills = None
        self.deaths = None
        self.alive = None
        self.game_class = None
        self.rank, self.team, self.connected, self.suicides, self.cp_captures, self.cp_defends = 0, 0, 0, 0, 0, 0
        self.cp_assists, self.cp_neutralizes, self.kit, self.position, self.cp_revives, self.cp_damageassists = 0, 0, 0, 0, 0, 0
        self.cp_passengerassists, self.cp_targetassists, self.idle = None, None, None
        self.vehicle_name, self.vehicle_type = None, None


class ServerCommando:
    def __init__(self, SOCKET):
        self.socket = SOCKET
        self.server = TCPBARE(ClientFace.ip, ClientFace.port, ClientFace.buffer, ClientFace.password, self.socket)
        self.usergroup = []
        self.playergroup = {}

    #properties
    @property
    def servername(self):
        _servername = None
        return _servername

    @servername.getter
    def servername(self):
        return self.server.send("exec sv.servername")

    @servername.setter
    def servername(self, value):
        self.server.send("exec sv.servername {0}".format(value))

    @property
    def server2ping(self):
        _ping = 0
        return _ping

    @server2ping.getter
    def server2ping(self):
        #dosomething
        return 3

    @property
    def serverURL(self):
        _url = None
        return _url

    @serverURL.getter
    def serverURL(self):
        return self.server.send("exec sv.bannerURL")

    @serverURL.setter
    def serverURL(self, _url):
        self.server.send("exec sv.bannerURL {0}".format(_url))

    @property
    def vipSlots(self):
        _vipSlots = 0
        return _vipSlots

    @vipSlots.getter
    def vipSlots(self):
        return self.server.send("exec sv.vipSlots")

    @vipSlots.setter
    def vipSlots(self, _amount):
        self.server.send("exec sv.vipSlots {0}".format(_amount))

    @property
    def roundsPerMap(self):
        _rounds = 0
        return _rounds

    @roundsPerMap.getter
    def roundsPerMap(self):
        return self.server.send("exec sv.roundsPerMap")

    @roundsPerMap.setter
    def roundsPerMap(self, _amount):
        self.server.send("exec sv.roundsPerMap {0}".format(_amount))
        
    @property
    def maxPlayers(self):
        _max = 0
        return _max

    @maxPlayers.getter
    def maxPlayers(self):
        #Can't go above 32 for P4F and 16(?) for BFH
        return int(self.server.send("exec sv.maxPlayers"))

    @maxPlayers.setter
    def maxPlayers(self, _amount):
        self.server.send("exec sv.maxPlayers {0}".format(_amount))

    @property
    def punkBuster(self):
        _bool = True
        return _bool

    @punkBuster.getter
    def punkBuster(self):
        _bool =  int(self.server.send("exec sv.punkbuster"))
        if _bool is 1:
            return True
        else:
            return False

    @punkBuster.setter
    def punkBuster(self, _bool):
        self.server.send("exec sv.punkbuster {0}".format(_bool))

    @property
    def welcomeMessage(self):
        _welcome = ""
        return _welcome

    @welcomeMessage.getter
    def welcomeMessage(self):
        return self.server.send("exec sv.welcomeMessage")

    @welcomeMessage.setter
    def welcomeMessage(self, _welcome):
        self.server.send("exec sv.welcomeMessage {0}".format(_welcome))

    @property
    def serverCommunity(self):
        _community = ""
        return _community

    @serverCommunity.getter
    def serverCommunity(self):
        return self.server.send("exec sv.serverCommunity")

    @serverCommunity.setter
    def serverCommunity(self, _community):
        self.server.send("exec sv.serverCommunity".format(_community))

    @property
    def rankship(self):
        _ranked = True
        return _ranked

    @rankship.getter
    def rankship(self):
        _booler = int(self.server.send("exec sv.ranked"))
        if _booler is 1:
            return True
        else:
            return False

    @rankship.setter
    def rankship(self, _boolint):
        self.server.send("exec sv.ranked {0}".format(_boolint))

    @property
    def plyerstostart(self):
        _playerstostart = 0
        return _playerstostart

    @plyerstostart.getter
    def plyerstostart(self):
        return int(self.server.send("exec sv.numPlayersNeededtoStart"))
    
    @plyerstostart.setter
    def plyerstostart(self, _amount):
        self.server.send("exec sv.numPlayersNeededtoStart {0}".format(_amount))
    
    @property
    def startDelay(self):
        _startDelay = 0
        return _startDelay

    @startDelay.getter
    def startDelay(self):
        return int(self.server.send("exec sv.startDelay"))

    @startDelay.setter
    def startDelay(self, _amount):
        self.server.send("exec sv.startDelay {0}".format(_amount))

    @property
    def notEnoughPlayersRestartDelay(self):
        _notenough = 0
        return _notenough

    @notEnoughPlayersRestartDelay.getter
    def notEnoughPlayersRestartDelay(self):
        return int(self.server.send("exec sv.notEnoughPlayersRestartDelay"))

    @notEnoughPlayersRestartDelay.setter
    def notEnoughPlayersRestartDelay(self, _amount):
        self.server.send("exec notEnoughPlayersRestartDelay {0}".format(_amount))

    @property
    def endDelay(self):
        _endDelay = 0
        return _endDelay

    @endDelay.getter
    def endDelay(self):
        return int(self.server.send("exec sv.endDelay"))

    @endDelay.setter
    def endDelay(self, _amount):
        self.server.send("exec sv.endDelay {0}".format(_amount))

    @property
    def manDownTime(self):
        _manDown = 0
        return _manDown

    @manDownTime.getter
    def manDownTime(self):
        return int(self.server.send("exec sv.manDownTime"))

    @manDownTime.setter
    def manDownTime(self, _amount):
        self.server.send("exec sv.manDownTime {0}".format(_amount))

    @property
    def ticketRatio(self):
        _tickerRatio = 100
        return _tickerRatio

    @ticketRatio.getter
    def ticketRatio(self):
        return int(self.server.send("exec sv.ticketRatio"))

    @ticketRatio.setter
    def ticketRatio(self, _amount):
        self.server.send("exec sv.ticketRatio {0}".format(_amount))

    @property
    def svpassword(self):
        _pass = None
        return _pass

    @svpassword.getter
    def svpassword(self):
        return self.server.send("exec sv.password")

    @svpassword.setter
    def svpassword(self, _pass):
        if self.rankship:
            self.server.send("exec sv.password {0}".format(_pass))
        else:
            #Whoa there cowboy... sv.password only applies if the server is unranked
            #But let's set it anyways...
            self.server.send("exec sv.password {0}".format(_pass))

    @property
    def autobalance(self):
        _booler = True
        return _booler

    @autobalance.getter
    def autobalance(self):
        _input = int(self.server.send("exec sv.autobalance"))
        if _input is 1:
            return True
        else:
            return False

    @autobalance.setter
    def autobalance(self, _bool):
        self.server.send("exec sv.autobalance {0}".format(_bool))

    @property
    def radioSpamInterval(self):
        _spam = 0
        return _spam

    @radioSpamInterval.getter
    def radioSpamInterval(self):
        return int(self.server.send("exec sv.radioSpamInterval"))

    @radioSpamInterval.setter
    def radioSpamInterval(self, _amount):
        self.server.send("exec radioSpamInterval {0}".format(_amount))

    @property
    def radioMaxSpamFlagCount(self):
        _spam = 0
        return _spam

    @radioMaxSpamFlagCount.getter
    def radioMaxSpamFlagCount(self):
        return int(self.server.send("exec sv.radioMaxSpamFlagCount"))

    @radioMaxSpamFlagCount.setter
    def radioMaxSpamFlagCount(self, _amount):
        self.server.send("exec sv.radioMaxSpamFlagCount {0}".format(_amount))

    @property
    def radioBlockedDurationTime(self):
        _block = 0
        return _block

    @radioBlockedDurationTime.getter
    def radioBlockedDurationTime(self):
        return int(self.server.send("exec sv.radioBlockedDurationTime"))

    @radioBlockedDurationTime.setter
    def radioBlockedDurationTime(self, _amount):
        self.server.send("exec sv.radioBlockedDurationTime {0}".format(_amount))

    @property
    def endofroundDelay(self):
        _delay = 0
        return _delay

    @endofroundDelay.getter
    def endofroundDelay(self):
        return int(self.server.send("exec sv.endofroundDelay"))

    @endofroundDelay.setter
    def endofroundDelay(self, _amount):
        self.server.send("exec sv.endofroundDelay {0}".format(_amount))

    ############################################################

    def getplayerlist(self):
        return self.server.send("")

    def runnextlevel(self, mapname):
        #admin.runnextlevel
        return self.server.send("")

    def runrestartlevel(self, mapname):
        #admin.restartmap
        return self.server.send("")

    def runkickpl(self, playername):
        #admin.kickplayer
        return self.server.send("exec admin.kickplayer {0}".format(playername))

    #RCON Methods
    def rconusers(self):
        self.usergroup = self.server.send("users").split("\n")
        return

    #MM Commands
    ##Announcer
    def listmsg(self):
        internal = self.server.send("announcer list").split("\n")
        return internal

    def addjoinmsg(self, message):
        return self.server.send("announcer addJoin '<{0}>'".format(message))

    def addtimemsg(self, message, start, repeat):
        return self.server.send("announcer addTimed  <{0}> <{1}> '<{2}>'".format(start, repeat, message))

    def removejoinmsg(self, joinid):
        return self.server.send("announcer removeJoin <{0}>".format(joinid))

    def removetimedmsg(self, timedid):
        return self.server.send("announcer removeTimed <{0}>".format(timedid))

    def removeall(self):
        return self.server.send("announcer .clearTimed"), self.server.send("announcer clearJoin")

    def removealljoin(self):
        return self.server.send("announcer clearJoin")

    def removealltimed(self):
        return self.server.send("announcer .clearTimed")

    ##Auto-balance
    def paramroundswitch(self, intindex):
        return self.server.send("mm setParam mm_autobalance roundSwitch {0}".format(intindex))

    #NOT RECOMMEDED FOR USE
    def paramallowcommander(self, blncom):
        return self.server.send("mm setParam mm_autobalance allowCommander {0}".format(blncom))

    def paramallowsqleader(self, blncom):
        return self.server.send("mm setParam mm_autobalance allowSquadLeader {0}".format(blncom))

    def paramallowsqmember(self, blncom):
        return self.server.send("mm setParam mm_autobalance allowSquadMember {0}".format(blncom))

    ##Ingame Commands
    def listiga(self):
        return self.server.send("iga listCmds")

    def listigaadmins(self):
        return self.server.send("iga listAdmins")

    def deligacmd(self, cmd):
        return self.server.send("iga delCmd <{0}>".format(cmd))

    def addigacmd(self, cmd, attri):
        return self.server.send("iga addCmd {0} {1}".format(cmd, attri))

    def addigaadmin(self, profile_or_name, premission):
        return self.server.send("iga addAdmin {0} {1}".format(profile_or_name, premission))

    def paramigaauth(self, value):
        return self.server.send("mm setParam mm_iga authLevel {0}".format(value))


class BF2CC:
    def __init__(self, SOCKET):
        self.socket = SOCKET
        self.server = TCPBARE(ClientFace.ip, ClientFace.port, ClientFace.buffer, ClientFace.password, self.socket)
        self.bf2ccsiarray = self.getbf2ccsi()
        self.internal = self.getbf2ccpl()

    @property
    def ticketsT1(self):
        _ticket = 0
        return _ticket

    @ticketsT1.getter
    def ticketsT1(self):
        return int(self.bf2ccsiarray[11])

    @property
    def ticketsT2(self):
        _ticket = 0
        return _ticket

    @ticketsT2.getter
    def ticketsT2(self):
        return int(self.bf2ccsiarray[16])

    @property
    def totalrounds(self):
        _total = 0
        return _total

    @totalrounds.getter
    def totalrounds(self):
        return int(self.bf2ccsiarray[30])

    @property
    def currentround(self):
        _current = 0
        return _current

    @currentround.getter
    def currentround(self):
        return int(self.bf2ccsiarray[31])

    @property
    def walltime(self):
        _walltime = 0
        return _walltime

    @walltime.getter
    def walltime(self):
        _waller = int(self.bf2ccsiarray[28])
        return datetime.datetime.fromtimestamp(_waller).strftime('%m-$d-$Y %H:%M:%S')

    def getbf2ccsi(self):
        grabarray = self.server.send("bf2cc si")
        grabarray = grabarray.replace("\n\x04", "").split("\t")
        return grabarray

    def getbf2ccchat(self):
        grab = self.server.send("bf2cc serverchatbuffer")
        grab = grab.replace("\n\x04", "").split("\r\r")
        return grab

    def getbf2ccpl(self):
        """
        Gets the bf2cc pl command from the bf2cc class. Response contains:
        0 p.pid
        1 p.name
        2 p.team
        3 p.ping
        4 p.connected
        5 p.valid
        6 p.isRemote
        7 p.isAiPlayer
        8 p.isAlive
        9 p.isManDown
        10 p.profileId
        11 p.isFlagHolder
        12 p.getSuicides
        13 p.timeToSpawn
        14 p.squadId
        15 p.isSquadLeader
        16 p.isCommander
        17 p.getSpawnGroup
        18 ip
        19 damage assists
        20 passenger assists
        21 target assists
        22 revives
        23 team damages
        24 team vehicle damages
        25 cp_captures
        26 cp_defends
        27 cp_assists
        28 neutralizes
        29 neutralizes assists
        30 suicides
        31 kills
        32 team kills
        33 vehicle type
        34 kit
        35 connectedAt
        36 deaths
        37 score
        38 vehicle name
        39 rank/level
        40 position
        41 idle
        42 cd key
        43 tk Punished
        44 tk Times Punished
        45 tk Times Forgiven
        46 vip
        47 nucleusId

        -Credit to: Vegabruda from the BFH forums: http://goo.gl/T8sA37
        :return:
        """
        grab = self.server.send("bf2cc pl")
        numberer = int(self.getnumpl())
        if numberer > 0:
            internal = grab.replace("\r\x04", "").split('\r')
        else:
            internal = grab.replace("\x04", "").split('\r')
        return internal

    #get info from BF2CC - some alts to PureCommands

    def getservername(self):
        """
        replaces the need to call server property, sv.servername
        :return:
        """
        return self.bf2ccsiarray[7]

    def getnumpl(self):
        """
        replaces the rcon command of
        :return:
        """
        return self.bf2ccsiarray[3]

    def getplayerlist(self):
        """
        Takes list split by "\r" from getbf2ccpl and splits it further by "\t" in order to have a multi-stepped list:
        >Parent List
            >Child List[0]
                >"playername"[1]
                >...[n]
            >...[n]

        Another list initializes itself by creating PlayerStruc() in the same amount of items in internal (represents
        amount of players). Use for-loop to pry open the Parent List (referred above) and assign each index to a certain
        object's PlayerStruc variable.
        >r List
            >PlayerStruc() Object #hash
                >playername = Parent List[Child List]["playername]
                >nucleus = ...
                >... = ...
            >...

        To access a certain entry => someplayeritem = someplayerlist[0].variablename
        Also, I'm pretty sure the list is ordered by the index (the same way the actual BF2CC pl response is called back
        in.
        :return r:
        """
        internal = self.getbf2ccpl()
        r = [PlayerStruc() for i in range(0, len(internal))]
        instance = []
        for i in range(0, len(internal)):
            instance.append(internal[i].split('\t'))
            r[i].playername = instance[i][1]
            r[i].alive = instance[i][8]
            r[i].connected = instance[i][4]
            r[i].cp_assists = instance[i][27]
            r[i].cp_captures = instance[i][25]
            r[i].cp_damageassists = instance[i][19]
            r[i].cp_defends = instance[i][26]
            r[i].cp_neutralizes = instance[i][28]
            r[i].cp_passengerassists = instance[i][20]
            r[i].cp_revives = instance[i][22]
            r[i].cp_targetassists = instance[i][21]
            r[i].deaths = instance[i][36]
            #r[i].game_class = instance[i][] not implemented
            r[i].idle = instance[i][41]
            r[i].kills = instance[i][31]
            r[i].kit = instance[i][34]
            r[i].nucleus = instance[i][47]
            r[i].ping = instance[i][3]
            r[i].position = instance[i][40]
            r[i].profile = instance[i][10]
            r[i].rank = instance[i][39]
            r[i].score = instance[i][37]
            r[i].suicides = instance[i][12]
            r[i].team = instance[i][2]
            r[i].vehicle_name = instance[i][38]
            r[i].vehicle_type = instance[i][33]
        return r

    def getchatresponse(self):
        gotcha = self.getbf2ccchat()
        r = [ChatStruct() for i in range(0, len(gotcha))]
        instance = []
        for i in range(0, len(gotcha)):
            instance.append(gotcha[i].split('\t'))
        del instance[-1]
        #timer = " {0} {1} {2}".format(datetime.now().year, datetime.now().month, datetime.now().day)
        for i in range(0, len(instance)):
            r[i].index = instance[i][0]
            r[i].playername = instance[i][1]
            r[i].noner = instance[i][2]
            r[i].type = instance[i][3]
            #r[i].time = time.strptime(instance[i][4] + timer, "[%H:%M:%S] %Y %m %d")
            r[i].time = instance[i][4]
            r[i].message = instance[i][5]
        return r