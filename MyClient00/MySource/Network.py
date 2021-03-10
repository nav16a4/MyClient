import time
import threading
import socket
from . import Packet
from . import Log
from . import Console
class Network:
    def __init__(self,ip,port,logfile=Log.DummyLogfile()):
        self.ip=ip
        self.port=port
        self.log = logfile
        return
    def recv(self):
        while True:
            print("Recv()\n")
            time.sleep(1)
        return
    def send(self,packet):
        result=0
        sendbyte=len(packet)
        result += self.socket.send(packet)
        while result < sendbyte:
            result+= self.socket.send(packet[result:])
        return
    def build(self, console):
        self.log.write("IP : {} PORT : {}\n".format(self.ip,self.port))
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

       
        self.socket.connect((self.ip,self.port))
       

        self.chatthread=threading.Thread(target=self.chat,args=(console,))
        self.chatthread.start()
        #self.sendthread.start()

        return
    def GetSocket(self):
        return self.socket
    
    def run(self):
        self.log.write("Run\n")
        self.chatthread.join()
        return
    
    def chat(self , console : Console.ConsoleIo ):
        inputlogger = Log.Log(self.log,console.read)
        packetlogger = Log.Log(self.log,Packet.makepacket)
        sendlogger = Log.Log(self.log,self.send)
        while True:
            #string = console.read()
            string = inputlogger.execute()
            #packet = Packet.makepacket(0,string.encode("euc-kr"))
            packet = packetlogger.execute(0,string.encode("euc-kr"))
            sendlogger.execute(packet)
            #self.send(packet)
