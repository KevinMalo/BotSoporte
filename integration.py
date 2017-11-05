import requests
from preguntas import Preguntas

query_get = requests.get(

    'https://api.dialogflow.com/v1/intents/64da54a0-4d74-4bc6-9494-bfbdbde35b4c?v=20150910',
    headers = {'Authorization':'Bearer af8f01865f994a5186d4ae0b0b250d11', 'Content-Type':'application/json'}

)

preguntas = Preguntas()
print (preguntas.consultar( {'Categoria'} ))

payload = {}

'''query_post = requests.post(

    'https://api.dialogflow.com/v1/intents?v=20150910', 
    headers = {'Authorization':'Bearer af8f01865f994a5186d4ae0b0b250d11', 'Content-Type':'application/json'},
    data = payload 
    
    )'''

#print( query_get.text )

#print( query_post.text )