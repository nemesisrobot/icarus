#Autor:Diego Silva
#Data:07/11/2019
#Descrição: Script para connectar no wifi

import network
import time
from machine import Pin

import network
import time
from machine import Pin

#instanciando classes para trabalhar com os recursos de rede e GPIO
ap_if = network.WLAN(network.AP_IF)
sta_if = network.WLAN(network.STA_IF)
pin  = Pin(0, Pin.OUT)
status = Pin(2, Pin.OUT)

#metodo para habilita o modo station, desabilitar access point e conexão no wifi
def activeStation(setting):
    ap_if.active(False)
    sta_if.active(True)
    sta_if.connect(setting.getSSID(),setting.getPassword())
    print(str(sta_if.isconnected()))

#nivel alto
def enableGPIO():
    pin.value(1)

#nivel baixo
def desableGPIO():
    pin.value(0)

#status atual
def statusGPIO():
    return int(pin.value())

#GPIO status conexão
def statusconnection(wifi):
	status.value(wifi)

#desconecta do wifi
def closeConnection():
	sta_if.disconnect()