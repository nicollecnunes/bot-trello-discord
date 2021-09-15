import requests
import json
from types import SimpleNamespace

def GetCardsMemberIsOn(id_membro):
    url = "https://api.trello.com/1/members/" + id_membro + "/cards"

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
    "GET",
    url,
    headers=headers
    )

    data = json.dumps(json.loads(response.text))
    data = data.split('manualCoverAttachment')

    resposta = ""
    
    for i in range(len(data)):
        if(i!=0):
            lista = data[i].split('"')
            resposta = resposta + (lista[4]) + ", "

    resposta = resposta[:-2]  

    #retorna a lista de cards que a pessoa ingressou
    return resposta





