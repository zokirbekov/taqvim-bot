import threading
import time

class TimeWorker(object):
    #TO DO -- time handling when namoz time comes
    #TO DO -- time handling when namoz time after 30 minutes
    #TO DO -- time handling when time is 00 : 00 and GET today namoz times
    def namozCames(self):
        print("Hello")
    def NamozCames(self,vaqt):
        print("Hello")
        t = threading.Timer(5,self.NamozCames,[vaqt],{})
        t.start()

    # def run(self):
    #     t1 = threading.Thread
    pass