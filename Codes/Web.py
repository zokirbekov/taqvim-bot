from grab import Grab
import requests
class WebWorker(object):
    #TO DO -- GET today namoz times from http://shosh.uz/namoz-vaqtlari-toshkent-shahri/

    def __init__(self,url,data):
        self.url = url
        self.data = data
        pass
    def sendData(self):
        return requests.get(url = self.url,params = self.data)
    pass
