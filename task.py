#Autor:Diego Silva
#Data:14/11/2019
#Descrição:Script para executa conexão/desconexão e execução de GPIO
import runfirmware as rn
import controlhardware as gp

#metodo de execução
def runtask():
	while(True):
		gp.activeStation()
		rn.control()
		gp.closeConnection()
		