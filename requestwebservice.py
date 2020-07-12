#Autor:Diego Silva
#Data:07/11/2019
#Descrição: Script para fazer request no webservice
import urequests
import json

headers = {'content-type':'application/json'}

#retorna dados do servidor
def getNotes(url_callbak):
    #faz requests, se a response for 200 ele retorna o json obtido
    response = urequests.get(url_callbak)
    if(response.status_code == 200):
        dados = str(response.text)
        dados = dados.replace("\n","")
        dados = dados.replace("[","")
        dados = dados.replace("]","")
        print('resposta servidor')
        print(str(response.text))
        return json.loads(dados)

#metódo faz post de status do device
def postStatusDevice(statusnow,url_callbak,device):
    payload = {'device':device,'corte':statusnow}
    resposta = urequests.post(url=url_callbak, data=json.dumps(payload), headers=headers)
    print(str(resposta.text))