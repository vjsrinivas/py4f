__author__ = 'Vijaysrinivas Rajagopal'

from datetime import datetime
import os


class ChatStruct:
    """
    Small class structure to help Kommand.getchatresponse()
    """
    __slots__ = ['index', 'time', 'playername', "type", "message", "noner", "all"]

    def __init__(self):
        self.index = None
        self.time = None
        self.playername = None
        self.type = None
        self.message = None
        self.noner = None


class ChatLog:
    """
    Responsible for retrieving and writing serverchat buffers into a /chat directory and in a .file
    """

    def __init__(self, CHATLOG="\chatlog\\"):
        self._isWriting = False
        self._dateReap = datetime
        self.restarttime = "23:59:59"
        self._dateLiteral = ""
        self._currentDir = os.getcwd() + CHATLOG
        self._getdirc()

    def _getdirc(self):
        """
        Creates a directory called "chatlog"
        :return nothing:
        """
        try:
            os.makedirs(self._currentDir, mode=0o77, exist_ok=True)
        except (OSError, Exception) as e:
            print(e)

    def writelog(self, x):
        """
        Creates a file called "CHATLOG[Month/Day/Year]" and appends to that file with the format of:
            [1  12:32:42    PlayerName: 'somethingsomethingsomething']
        :param x - the source of the chatbuffer list (the return product of Kommands.getchatresponse():
        :return nothing:
        """
        self._dateLiteral = "{}:{}:{}".format(self._dateReap.now().hour, self._dateReap.now().minute,
                                              self._dateReap.now().second)
        if self._dateLiteral is self.restarttime:
            print("\r\n'MIDNIGHT SP000KY - Generating new file...\r\n'")
        try:
            filename = "CHATLOG[{0}.{1}.{2}].txt".format(self._dateReap.now().month, self._dateReap.now().day,
                                                     self._dateReap.now().year)
            logger = open(self._currentDir + filename, mode="a+")
            _fileofsize = os.stat(self._currentDir+filename).st_size
            if _fileofsize is 0:
                logger.write(
                    " ********************\n|| GENERATED ON: {} ||\n ********************\r\n".format(self._dateLiteral)
                )
            for i in range(0, len(x)):
                template = "[{0}\t{1}\t{2}:\t'{3}']\r\n".format(x[i].index, x[i].time, x[i].playername, x[i].message)
                logger.write(template)
        except Exception as e:
            print(e)