#Autor:Diego Silva
#Data:07/11/2019
#Descrição: Script para fazer request no webservice
import urequests
import json

headers = {'content-type':'application/json'}

#retorna dados do servidor
def getNotes():
    #faz requests, se a response for 200 ele retorna o json obtido
    response = urequests.get('http://192.168.15.15:5000/notaservico/xpto1')
    if(response.status_code == 200):
        dados = str(response.text)
        dados = dados.replace("\n","")
        dados = dados.replace("[","")
        dados = dados.replace("]","")
        print('resposta servidor')
        print(str(response.text))
        return json.loads(dados)

#metódo faz post de status do device
def postStatusDevice(statusnow):
    payload = {'device':'xpto1','corte':statusnow}
    resposta = urequests.post(url='http://192.168.15.15:5000/dispositivostatus', data=json.dumps(payload), headers=headers)
    print(str(resposta.text))