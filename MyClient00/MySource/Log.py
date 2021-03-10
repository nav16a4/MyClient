import inspect
import datetime
class LogFile:
    def __init__(self,*args):
        self.files = args
    def write(self,str):
        for i in self.files:
            i.write(str)
class DummyLogfile(LogFile):
    def __init__(self,*args):
        return
    def write(self,str):
        return
class Log:
    def __init__(self,logfile,func):
        self.func=func
        self.log=logfile
        self.name="Func:{}".format(func.__name__)
    def getcallstring(self,num):

        callerframerecord=inspect.stack()[num]
        frame=callerframerecord[0]
        info = inspect.getframeinfo(frame)
        return ("File:{},Func:{},Line:{}".format(info.filename.split("\\")[-1] ,info.function,info.lineno))

    def execute(self,*args):
        argument = "args:{}".format(args)
        
        time = datetime.datetime.now()
        callfrom= self.getcallstring(2)

        self.log.write("[{}][{}][{}][{}] Begin\n".format(time,callfrom,self.name,argument))

        result = self.func(*args)
        time = datetime.datetime.now()

        self.log.write("[{}][{}][{}][{}][return:{}] End\n".format(time,callfrom,self.name,argument,result))
        return result

