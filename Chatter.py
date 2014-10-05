__author__ = 'Admin'

from datetime import datetime
import os


class ChatStruct:
    __slots__ = ['index', 'time', 'playername', "type", "message", "noner", "all"]

    def __init__(self):
        self.index = None
        self.time = None
        self.playername = None
        self.type = None
        self.message = None
        self.noner = None


class ChatLog:
    def __init__(self, CHATLOG="\chatlog\\"):
        self._isWriting = False
        self._dateReap = datetime
        self._currentDir = os.getcwd() + CHATLOG
        self._getdirc()

    def _getdirc(self):
        try:
            os.makedirs(self._currentDir, mode=0o77, exist_ok=True)
        except (OSError, Exception) as e:
            print(e)

    def writelog(self, x):
        try:
            filename = "CHATLOG[{0}.{1}.{2}]".format(self._dateReap.now().month, self._dateReap.now().day,
                                                     self._dateReap.now().year)
            logger = open(self._currentDir+filename, mode="a+")
            template = None
            for i in range(0, len(x)):
                template = "[{0}  {1} {2}: '{3}']\r\n".format(x[i].index, x[i].time, x[i].playername, x[i].message)
                logger.write(template)
        except Exception as e:
            print(e)