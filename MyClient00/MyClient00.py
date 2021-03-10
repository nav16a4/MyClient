from MySource import Network
from MySource import Log
from MySource import Console
import datetime
import re
import sys
import threading

def test1(a,b,c,d):
    print("{} {} {} {} !!!!".format(a,b,c,d))

def timename():
    time ="{}".format(datetime.datetime.now())
    myre=re.compile("[0-9]+")
    reresult=myre.findall(time)
    name = "{}{}{}_{}h{}m{}.{}s.txt".format(reresult[0],reresult[1],reresult[2],reresult[3],reresult[4],reresult[5],reresult[6])
    return name


def main() :
    print("main")
    logfilename = timename()
  
   
    console = Console.ConsoleIo()

    #logfilename = "{}.txt".format()
    #print(logfile)
    logfile = open(logfilename,'w')
    log = Log.LogFile(logfile,sys.stdout)
    log.write("야야야야야야야\n")
    
    logger = Log.Log(log,test1)
    logger.execute(5,6,7,8)

    client = Network.Network("172.16.3.16",44004,log)
    client.build(console)



    client.run()

    
    


#
if __name__=='__main__':
    main()