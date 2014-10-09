__author__ = 'Vijaysrinivas Rajagopal'

import socket, hashlib


class TCPBARE:

    """
    Basic setup for a TCP connection to an RCON-enabled server.
    Supported bases => BF2, BFH, BFP4F(Main), BF2142
    """

    def __init__(self, IP, PORT, BUFFER, RCONPW, SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
        self.IP = IP
        self.PORT = PORT
        self.BUFFER = BUFFER
        self.RCONPW = RCONPW
        #s is entirety of the framework. You must provide your own instance (in ClientFace)
        self.s = SERVER
        #server-properties

    def connect(self):
        """
        Establishes connection to a certain RCON-enabled server.
        IP Address and Port Number are sensitive and should be typed with precision.
        :return bool of if the try went correctly:
        """
        try:
            self.s.connect((self.IP, self.PORT))
            print("Connecting...")
            return True
        except Exception as e:
            print(e)
            return False

    def close(self):
        """
        Closes connection to active client, and then checks to see if connection has actually been dropped.
        Returns 0 for connection dropped through ECONN. Raises for possibly unexpected exceptions
        :return 0 or raise:
        """
        self.s.close()

    def auth(self):
        """
        Authorizes connection to RCON port with the provided RCON password.
        MD5 encryption includes the seed and the password. hashlib requires seed+pw to be encoded into a supported type;
        Data sent to and fore are encoded in bytes by default. Use decode("type") to convert to usable string
        :return bool of success:
        """
        inkeep = 0
        authsuccess = False
        while True:
            print(inkeep)
            inkeep += 1
            refdata = self.s.recv(self.BUFFER)
            truedata = refdata.decode("utf-8")
            if inkeep == 4:
                print("[CRITICAL ERROR: INKEEPER OVERFLOWED; INCORRECT ASSIGNMENTS]")
                break
            if truedata[:5] == "### D":
                digestseed = truedata[17:]
                digestseed = digestseed[:16]
                print(digestseed)
                break
            else:
                continue

        md5pass = hashlib.md5(digestseed.encode("utf-8") + self.RCONPW.encode("utf-8")).hexdigest()
        RCONPASS = "login " + md5pass + '\n'
        self.s.send(RCONPASS.encode(encoding="utf-8"))
        retrieve = self.read()
        if "successful" in retrieve: authsuccess = True
        else: authsuccess = False
        return authsuccess

    def send(self, command):

        """
        Sends command parameter through the connected socket. Prefixed 0x02 for server response ending in 0x04.
        Recommended function for sending RCON commands. Also uses read function to return output.
        :param command - Admin input for command. Requires proper command; console commands starting with "exec":
        :return read(data):
        """
        package = '\2' + command + '\n'
        encodepack = str.encode(package)
        self.s.send(encodepack)
        return self.read()

    def debug__send__(self, command="NULL"):
        """
        NOT INTENDED FOR PRODUCTION USE - Same documentation as send function but does not incorporate the prefix char.
        :param command - Admin input for command. Requires proper command; console commands starting with "exec":
        :return read(data):
        """
        package = command + '\n'
        encodepack = str.encode(package)
        self.s.send(encodepack)
        return self.read()

    def read(self):

        """
        NOT RECOMMENDED FOR EXTERNAL USE. Intended use is internal retrieval for the send command (both types?)
        :return data:
        """
        while True:
            rawdata = self.s.recv(self.BUFFER)
            if rawdata[-3:] != 'x04':
                data = rawdata.decode("utf-8")
                #print(data)
                data = self.cleanup(data)
                return data
            else:
                continue

    def cleanup(self, inputparam):
        if '\n\x04' in inputparam:
            inputparam = inputparam.replace("\n\x04", "")
        return inputparam
