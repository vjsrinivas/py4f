__author__ = 'Vijaysrinivas Rajagopal'

from RCONBase import TCPBARE
from Chatter import*
import ClientFace
import datetime
import threading, time, difflib


class PlayerStruc:
    """
    Class is used for reference when storing information given by the command bf2cc pl.
    """

    __slots__ = ['index', 'playername', 'nucleus', 'profile', 'score', 'ping', 'kills', 'deaths', 'alive', 'game_class',
                 'rank', 'team', 'connected', 'suicides', 'cp_captures', 'cp_defends', 'cp_assists', 'cp_neutralizes',
                 'kit', 'position', 'vehicle_name', 'vehicle_type', 'isAI', 'cp_revives', 'cp_damageassists',
                 'cp_passengerassists', 'cp_targetassists', 'idle']

    def __init__(self):
        self.index = 0
        self.playername = None
        self.nucleus = None
        self.profile = None
        self.score = 0
        self.ping = 0
        self.kills = 0
        self.deaths = 0
        self.alive = False
        self.game_class = None
        self.rank, self.team, self.connected, self.suicides, self.cp_captures, self.cp_defends = 0, None, False, 0, 0, 0
        self.cp_assists, self.cp_neutralizes, self.kit, self.position, self.cp_revives, self.cp_damageassists = 0, 0, None, (), 0, 0
        self.cp_passengerassists, self.cp_targetassists, self.idle = 0, 0, 0
        self.vehicle_name, self.vehicle_type = None, None
        self.isAI = False


class MapStruc:
    """
    Small class structure helps split a maplist.list's return into usable parts
    """
    __slots__ = ['mapindex', 'mapname', 'gamemode', 'numpl']

    def __init__(self):
        self.mapindex = -1
        self.mapname = None
        self.gamemode = None
        self.numpl = 0


class ServerCommando:
    def __init__(self, SOCKET):
        self.socket = SOCKET
        self.server = TCPBARE(ClientFace.ip, ClientFace.port, ClientFace.buffer, ClientFace.password, self.socket)
        self.usergroup = []
        self.playergroup = {}

    #properties
    @property
    def modules(self):
        _internal = []
        return _internal

    @modules.getter
    def modules(self):
        _internal = self.server.send("mm listModules").split("\n")
        _external = {}
        for i in range(len(_internal)):
            stringer = _internal[i]
            if _internal[i][-10:] == " running )":
                _external[_internal[i][1:stringer.find(" v")]] = "running"
            else:
                _external[_internal[i][:10]] = "loaded"
        return _external

    def startmodule(self, modulename):
        self.server.send("mm startModule {0}".format(modulename))

    def stopmodule(self, modulename):
        self.server.send("mm stopModule {0}".format(modulename))

    def loadmodule(self, modulename):
        self.server.send("mm loadModule {0}".format(modulename))

    def reloadmodule(self, modulename):
        self.server.send("mm reloadModule {0}".format(modulename))

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
        return int(self.server.send("exec sv.roundsPerMap"))

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
        _bool = int(self.server.send("exec sv.punkbuster"))
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

    def runnextlevel(self):
        #admin.runnextlevel
        return self.server.send("exec admin.runnextlevel")

    def runrestartlevel(self):
        #admin.restartmap
        return self.server.send("exec admin.restartMap")

    def runkickpl(self, playerid, reason):
        return self.server.send("kick '{0}' '{1}'".format(playerid, reason))

    def runkickplalt(self, playername):
        #admin.kickplayer
        return self.server.send("exec admin.kickplayer {0}".format(playername))

    def runbanpl(self, playerid, reason):
        return self.server.send("ban {0} \"{1}\"".format(playerid, reason))

    def listplayers(self):
        #admin.listPlayers
        return self.server.send("exec admin.listPlayers")

    #Maps
    @property
    def maplistall(self):
        _internal = []
        return _internal

    @maplistall.getter
    def maplistall(self):
        return self.server.send("exec maplist.listall").split('\n')

    @property
    def maplist(self):
        _maplist = []
        return _maplist

    @maplist.getter
    def maplist(self):
        holder = self.server.send("exec mapList.list").replace(":", "")
        holder = holder.split("\n")
        holdee = []
        _mapee = [MapStruc() for i in range(0, len(holder))]
        for i in range(0, len(holder)):
            holdee.append(holder[i].split(' '))
            _mapee[i].mapindex = int(holdee[i][0])
            _mapee[i].mapname = holdee[i][1]
            _mapee[i].gamemode = holdee[i][2]
            _mapee[i].numpl = int(holdee[i][3])
        return _mapee

    @property
    def nextmap(self):
        _next = None
        return _next

    @nextmap.getter
    def nextmap(self):
        return int(self.server.send("exec admin.nextLevel"))

    @property
    def currentmap(self):
        _current = 0
        return _current

    @currentmap.getter
    def currentmap(self):
        return int(self.server.send("exec mapList.current"))

    @property
    def mapcount(self):
        _count = 0
        return _count

    @mapcount.getter
    def mapcount(self):
        return int(self.server.send("exec mapList.mapCount"))

    def appendmap(self, mapname, gamemode, numpl):
        return self.server.send("exec mapList.append {0} {1} {2}".format(mapname, gamemode, numpl))

    def insertmap(self, index, mapname, gamemode, numpl):
        return self.server.send("exec mapList.insert {0} {1} {2} {3}".format(index, mapname, gamemode, numpl))

    def savemapcon(self):
        return self.server.send("exec mapList.save")

    def reloadmapcon(self):
        return self.server.send("exec mapList.reload")

    def clearmaplist(self):
        return self.server.send("exec mapList.clear")

    def removemaplist(self, index):
        return self.server.send("exec mapList.remove {0}".format(index))

    #RCON Methods
    def rconusers(self):
        self.usergroup = self.server.send("users").split("\n")
        return

    #MM Commands
    ##Announcer
    @property
    def listmsg(self):
        _internal = []
        return _internal

    @listmsg.getter
    def listmsg(self):
        return self.server.send("announcer list").split("\n")

    @property
    def listjoinmsg(self):
        return []

    @listjoinmsg.getter
    def listjoinmsg(self):
        _internal = self.server.send("announcer list").split("\n")
        if _internal[0] == "No join messages":
            return _internal[0]
        else:
            return _internal[0:(_internal.index("Timed messages:")-1)]

    @property
    def listtimemsg(self):
        _internal = self.server.send("announcer list").split("\n")
        _timed = _internal.index("Timed messages:")
        if _internal[_timed] == "No timed messages":
            return _internal[_timed]
        else:
            return _internal[_timed:]

    def addjoinmsg(self, message):
        return self.server.send("announcer addJoin '{0}'".format(message))

    def addtimemsg(self, message, start, repeat):
        return self.server.send("announcer addTimed  {0} {1} '{2}'".format(start, repeat, message))

    def removejoinmsg(self, joinid):
        for i in range(0, len(joinid)):
            if i == 0:
                self.server.send("announcer removeJoin {0}".format(joinid[i]))
            else:
                self.server.send("announcer removeJoin {0}".format(joinid[i]-1))

    def removetimedmsg(self, timedid):
        return self.server.send("announcer removeTimed {0}".format(timedid))

    def removeall(self):
        return self.server.send("announcer clearTimed"), self.server.send("announcer clearJoin")

    def removealljoin(self):
        return self.server.send("announcer clearJoin")

    def removealltimed(self):
        return self.server.send("announcer clearTimed")

    def removealltimedalt(self):
        return self.server.send("newrcon clearLogin")


    ##Auto-balance
    @property
    def paramroundswitch(self):
        _output = None
        return _output

    @paramroundswitch.setter
    def paramroundswitch(self, intindex):
        self.server.send("mm setParam mm_autobalance roundSwitch {0}".format(intindex))
        self.server.send("mm saveConfig")

    #NOT RECOMMEDED FOR USE
    def paramallowcommander(self, blncom):
        return self.server.send("mm setParam mm_autobalance allowCommander {0}".format(blncom)), self.server.send("mm saveConfig")

    def paramallowsqleader(self, blncom):
        return self.server.send("mm setParam mm_autobalance allowSquadLeader {0}".format(blncom)), self.server.send("mm saveConfig")

    def paramallowsqmember(self, blncom):
        return self.server.send("mm setParam mm_autobalance allowSquadMember {0}".format(blncom)), self.server.send("mm saveConfig")

    ##Ingame Commands
    def listiga(self):
        return self.server.send("iga listCmds")

    def listigaadmins(self):
        return self.server.send("iga listAdmins")

    def deligacmd(self, cmd):
        return self.server.send("iga delCmd {0}".format(cmd))

    def addigacmd(self, cmd, attri):
        return self.server.send("iga addCmd {0} {1}".format(cmd, attri))

    def addigaadmin(self, profile_or_name, premission):
        return self.server.send("iga addAdmin {0} {1}".format(profile_or_name, premission))

    def paramigaauth(self, value):
        return self.server.send("mm setParam mm_iga authLevel {0}".format(value))

    ##Chat to
    def sayall(self, msg):
        return self.server.send("exec game.sayAll \"{0}\"".format(msg))

    def sayprivate(self, index, msg):
        return self.server.send("exec game.sayToPlayerWithId {0} \"{1}\"".format(index, msg))

    ##mm_kicker

    @property
    def listwords(self):
        return []

    @listwords.getter
    def listwords(self):
        return self.server.send("kicker listWords").split("\n")

    def addbanpattern(self, word):
        return self.server.send("addBanPattern {0}".format(word))

    def addbanword(self, word):
        return self.server.send("addBanWord {0}".format(word))

    def addkickpattern(self, word):
        return self.server.send("addKickPattern {0}".format(word))

    def addkickword(self, word):
        return self.server.send("addKickWord {0}".format(word))

    def clearbanpattern(self):
        return self.server.send("clearBanPatterns")

    def clearbanwords(self):
        return self.server.send("clearBanWords")

    def clearkickpattern(self):
        return self.server.send("clearKickPatterns")

    def clearkickwords(self):
        return self.server.send("clearKickWords")

    def removebanpattern(self, word):
        return self.server.send("removeBanPattern {0}".format(word))

    def removebanword(self, word):
        return self.server.send("removeBanWord {0}".format(word))

    def removekickpattern(self, word):
        return self.server.send("removeKickPattern {0}".format(word))

    def removekickword(self, word):
        return self.server.send("removeKickWord {0}".format(word))

    def setmaxping(self, value):
        return self.server.send("mm mm_kicker maxPing {0}".format(value))

    def setminping(self, vaulue):
        return self.server.send("mm mm_kicker minPing {0}".format(vaulue))


class BF2CC:
    """
    ALL information concerning the bf2cc module.
    Class contains properties that can be get/set and functions that return an array or nothing for an action
    """

    def __init__(self, SOCKET):
        self.socket = SOCKET
        self.server = TCPBARE(ClientFace.ip, ClientFace.port, ClientFace.buffer, ClientFace.password, self.socket)
        self.bf2ccsiarray = self.getbf2ccsi()
        self.internal = self.getbf2ccpl()
        self.update = False
        self.counter = 0
        self.reminder = []
        self.gotcha = []
        self.surrender = []

        ### NOT FULLY TESTED
        bkthread = threading.Thread(name='threader', target=self.__recall, args=())
        if self.update is True:
            bkthread.daemon = True
            bkthread.start()
        else:
            return
        ### INTENDED FOR CLIENT-SIDE USE. USING ON ANYTHING ELSE MIGHT RESULT IN UNEXPECTED CONSEQUENCES

    @property
    def numofplayers(self):
        _players = 0
        return _players

    @numofplayers.getter
    def numofplayers(self):
        return int(self.bf2ccsiarray[3])

    @property
    def ticketsT1(self):
        _ticket = 0
        return _ticket

    @ticketsT1.getter
    def ticketsT1(self):
        return self.ticketstartT1 - int(self.bf2ccsiarray[11])

    @property
    def ticketstartT1(self):
        _tickerstart = 0
        return _tickerstart

    @ticketstartT1.getter
    def ticketstartT1(self):
        return int(self.bf2ccsiarray[10])

    @property
    def ticketsT2(self):
        _ticket = 0
        return _ticket

    @ticketsT2.getter
    def ticketsT2(self):
        return self.ticketstartT2 - int(self.bf2ccsiarray[16])

    @property
    def ticketstartT2(self):
        _tickerstart = 0
        return _tickerstart

    @ticketstartT2.getter
    def ticketstartT2(self):
        return int(self.bf2ccsiarray[15])

    @property
    def gamestate(self):
        _state = "N/A"
        return _state

    @gamestate.getter
    def gamestate(self):
        _holder = int(self.bf2ccsiarray[1])
        if _holder is 1:
            return "Playing"
        elif _holder is 2:
            return "End Game"
        elif _holder is 0:
            #not sure
            return "Pre-game"
        else:
            return "Some other state I forgot about"

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
        _waller = float(self.bf2ccsiarray[28])
        return datetime.datetime.fromtimestamp(_waller).strftime('%m-%d-%Y %H:%M:%S')

    def getbf2ccsi(self):
        """
        Gets the bf2cc si command from the bf2cc class. Response contains:
        0	version
        1	current game status
        2	max players
        3	players
        4	joining
        5	map name
        6	next map name
        7	server name
        8	team 1 name
        9	team 1 ticket state
        10	team 1 start tickets
        11 team 1 tickets
        12	disabled (always 0)
        13	team 2 name
        14	team 2 ticket state
        15	team 2 start tickets
        16 team 2 tickets
        17 disabled (always 0)
        18	elapsed round time
        19	remaining time
        20	game mode
        21	mod dir
        22	world size
        23	time limit
        24	autobalance
        25 ranked status
        26 team 1 count
        27 team 2 count
        28 wall time
        29 reserved slots
        30 total rounds
        31 current round

        -Credit to: Vegabruda from the BFH forums: http://goo.gl/T8sA37
        :return:
        """
        grabarray = self.server.send("bf2cc si")
        grabarray = grabarray.replace("\n\x04", "").split("\t")
        return grabarray

    def getbf2ccchat(self):
        grab = self.server.send("bf2cc serverchatbuffer")
        grab = grab.replace("\n\x04", "").split("\r\r")
        del grab[-1]
        return grab

    #Recommended not to change
    def chatbuffer(self, value):
        return self.server.send("mm setParam mm_bf2cc chatBufferSize {0}".format(value)), self.server.send("mm saveConfig")

    def chatformat(self, chatformat):
        return self.server.send("mm setParam mm_bf2cc serverchatFormat \"{0}\"".format(chatformat)), self.server.send("mm saveConfig")

    def printRunningConfig(self):
        return self.server.send("mm printRunningConfig")
    ###

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
        numberer = self.numofplayers
        if numberer > 0:
            internal = grab.replace("\r\x04", "").split('\r')
        else:
            internal = grab.replace("\x04", "").split('\r')
        return internal

    #get info from BF2CC - some alts to PureCommands

    @property
    def servername(self):
        """
        replaces the need to call server property, sv.servername
        :return:
        """
        _part = ""
        return _part

    @servername.getter
    def servername(self):
        return self.bf2ccsiarray[7]

    @servername.setter
    def servername(self, value):
        self.server.send("exec sv.servername {0}".format(value))

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
        if self.numofplayers > 0:
            for i in range(0, len(internal)):
                instance.append(internal[i].split('\t'))
                r[i].index = int(instance[i][0])
                r[i].playername = instance[i][1]
                r[i].alive = bool(instance[i][8])
                r[i].connected = bool(instance[i][4])
                r[i].cp_assists = int(instance[i][27])
                r[i].cp_captures = int(instance[i][25])
                r[i].cp_damageassists = int(instance[i][19])
                r[i].cp_defends = int(instance[i][26])
                r[i].cp_neutralizes = int(instance[i][28])
                r[i].cp_passengerassists = int(instance[i][20])
                r[i].cp_revives = int(instance[i][22])
                r[i].cp_targetassists = int(instance[i][21])
                r[i].deaths = int(instance[i][36])
                #r[i].game_class = instance[i][] not implemented
                r[i].idle = int(instance[i][41])
                r[i].kills = int(instance[i][31])
                r[i].kit = instance[i][34]
                r[i].nucleus = instance[i][47]
                r[i].ping = int(instance[i][3])
                for position in [instance[i][40].split(',')]:
                    r[i].position = [float(position[0]), float(position[1]), float(position[2])]
                r[i].profile = instance[i][10]
                r[i].rank = int(instance[i][39])
                r[i].score = int(instance[i][37])
                r[i].suicides = int(instance[i][12])
                r[i].team = int(instance[i][2])
                r[i].vehicle_name = instance[i][38]
                r[i].vehicle_type = instance[i][33]
            return r
        else:
            return

    def getchatresponse(self, filterout = None):
        """
        Retrieves bf2cc serverchatbuffer's repsonse and splits it into whole chunks (consisting of a whole chat instance)
        Then, these chunks are split further into their respective fields. (Similar to getplayerlist()) and processed
        through ChatStruc class for a return.
        :return r as a ChatStruc list:
        """
        getcha = self.getchatraw()
        if getcha is None:
            return None
        else:
            r = [ChatStruct() for i in range(0, len(getcha))]
        instance = []
        for i in range(0, len(getcha)):
            instance.append(getcha[i].split('\t'))
        #timer = " {0} {1} {2}".format(datetime.now().year, datetime.now().month, datetime.now().day)
        for i in range(0, len(instance)):
            r[i].index = instance[i][0]
            r[i].playername = instance[i][1]
            r[i].noner = instance[i][2]
            r[i].type = instance[i][3]
            #r[i].time = time.strptime(instance[i][4] + timer, "[%H:%M:%S] %Y %m %d")
            r[i].time = instance[i][4]
            r[i].message = instance[i][5]
        if filterout is None:
            return r
        else:
            superlative = []
            for e in range(0, len(r)):
                if r[e].message.find("|ccc|") == -1:
                    superlative.append(r[e])
                else:
                    continue
            return superlative

    def getchatraw(self):
        self.surrender = []
        if self.counter == 0:
            self.reminder = self.getbf2ccchat()
            self.surrender = self.reminder
        self.counter += 1
        print("{} >>>>>>>>".format(self.counter))
        self.gotcha = self.getbf2ccchat()
        if self.counter % 8 == 0:
            self.reminder = self.getbf2ccchat()
        else:
            for i,s in enumerate(difflib.ndiff(self.gotcha, self.reminder)):
                if s[0] == ' ':
                    if not self.surrender:
                        self.surrender = []
                    else: continue
                elif s[0] == '-' or s[0] == '+':
                    print("Difference detected")
                    try:
                        suerma = self.gotcha.index(self.reminder[-1])
                    except TypeError:
                        self.gotcha = []
                        return self.surrender
                    self.surrender = self.gotcha[suerma+1:]
                    self.reminder = self.gotcha
                    return self.surrender
                elif s[0] == "?":
                    print("unknown")
                else:
                    continue
        return self.surrender

    def __recall(self):
        while self.update is True:
            self.bf2ccsiarray = self.getbf2ccsi()
            self.internal = self.getplayerlist()
            time.sleep(3) #seconds
            print("Executed")