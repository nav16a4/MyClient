import sys
import msvcrt
class ConsoleIo:
     def __init__(self,stream=sys.stdout,set="utf-8"):
         self.stream=stream
         self.bytearray=bytearray()
         self.set=set
     def write(self,str):
         #동기화
         self.stream.write("\t\t[{}]\n".format(str))
         self.stream.write(self.bytearray.decode(self.set))
         return
     def read(self):
         flag=True
         while True==flag:
             char = msvcrt.getwche()
             if u'\r'==char:
                self.stream.write('\n')
                char=u'\0'
                flag=False
             self.bytearray.extend(char.encode(self.set))

         string="{}".format(self.bytearray.decode(self.set))
         self.bytearray.clear()
         return string
