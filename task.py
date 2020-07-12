#Autor:Diego Silva
#Data:14/11/2019
#Descrição:Script para executa conexão/desconexão e execução de GPIO
import runfirmware as rn
import controlhardware as gp
from readconfig import *
#metodo de execução
def runtask():
	#lendo arquivo de configuração
	datafile = ReadDataConfig()
	file = datafile.readData()

	#fazendo parser para json
	filejson = datafile.parserStringtoDict(datafile.readLines(file))
	datafile.closeData(file)
	setting = SettingsDevice(filejson)

	while(True):
		gp.activeStation(setting)
		rn.control(setting)
		gp.closeConnection()
		