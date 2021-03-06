#Autor:Diego Silva
#Data:14/11/2019
#Descrição: codigo responsavel pelo controle do GPIO

import requestwebservice as rq
import controlhardware as gp
import time


#metodo para execução do GPIO
def control(setting):
    #aguarda um minuto e verifica se existe nota
    time.sleep(60)
    response = rq.getNotes(setting.getUrlNotes())

    #1 executa nota de religa
    if(1 == int(response['corte'])):
        gp.enableGPIO()

    #0 executa nota de desliga
    if(0 == int(response['corte'])):
        gp.desableGPIO()

    #atualizando status do device
    status = gp.statusGPIO()
    print(type(status))
    print(status)
    rq.postStatusDevice(status,setting.getUrlStatus(),setting.getDeviceName())
