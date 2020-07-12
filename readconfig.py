#Autor:Diego Silva
#Data:12/07/2020
#Descrição:Script para leitura de arquivo de configuração

import json

#classe para abrir arquivo
class ReadDataConfig:

    #abre arquivo
    def readData(self):
        f = open('config.json','r')
        return f
    
    #leitura de linha de arquivo
    def readLines(self, f):
        return f.read()

    #parser de string para dicionario
    def parserStringtoDict(self, dataread):
        return json.loads(dataread)
    
    #fechando leitura de arquivo
    def closeData(self, f):
        f.close()

class SettingsDevice:

    def __init__(self, datajson):
        self._datajson = datajson

    #método com url de post de status    
    def getUrlStatus(self):
        return '{}{}'.format(self._datajson['host'],self._datajson['post'])

    #metodo com url para pegar notas
    def getUrlNotes(self):
        return '{}{}{}'.format(self._datajson['host'],self._datajson['get'],self._datajson['device'])

    #metodo para ssid da rede wifi
    def getSSID(self):
        return '{}'.format(self._datajson['ssid'])

    #metodo para password do wifi
    def getPassword(self):
        return '{}'.format(self._datajson['password'])

    #metodo para retornar nome do dispositivo
    def getDeviceName(self):
        return '{}'.format(self._datajson['device'])
    


