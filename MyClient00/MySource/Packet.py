import sys
#class Data:
#    def __init__(self,size,value):
#        self.data = value
#        self.size = size
def makepacket(type : int ,data : object):
    buffer = bytearray(2)
    buffer[1]=type
    buffer.extend(data)
    buffer[0]= len(buffer)

    return buffer
    
class Packet:
    def __init__(self):
        self.buffer = bytearray(2)
        self.size = 2
        self.type = 0
        return

    def SetType(self,type):
        self.type=type
        return 

    def push_back(self,databyte: int,data ):
        
        pushed = data.to_bytes(databyte,sys.byteorder)

        self.buffer.extend(pushed)
        self.size=len(self.buffer)
        return

