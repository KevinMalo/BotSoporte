import requests
from datos import Datos

# Request GET for queries
'''
query_get = requests.get(

    'https://api.dialogflow.com/v1/intents/ID_INTENT?v=20150910',
    headers = {'Authorization':'Bearer af8f01865f994a5186d4ae0b0b250d11', 'Content-Type':'application/json'}

)
'''

#Read the questions and answers of my DB
datos = Datos()

#Encontrar todas las Categorias
categorias_filtro = datos.consultar( {} )

categorias = []
 

for i in categorias_filtro:

    ####################################################################
    categorias.append(i["Categoria"]) #espanhol

    #categorias.append(i['Categoria_en']) #ingles
    ####################################################################

#Usando las categorias para traer las preguntas y respuestas que hagan match con ellas

categorias_filtradas = list(set(categorias)) #Borrando todas las categorias repetidas

print(categorias_filtradas)

for cat in categorias_filtradas:
    
    cat = str(cat)
    ####################################################################
    dats = datos.consultar( {"Categoria":{"$in":[cat]}} ) #espanhol
    #dats = datos.consultar( {"Categoria_en":{"$in":[cat]}} ) #ingles
    ####################################################################

    respuestas = []

    preguntas = []

    for dat in dats:
        
        try:

            ####################################################################
            #print( dat["Pregunta"], "\n", dat["Respuesta"], "\n" )
            #print( dat['Pregunta_en'], '\n', dat['Respuesta_en'] )  para ingles

            respuestas.append(dat["Respuesta"]) #Espanhol
            #respuestas.append(dat["Respuesta_en"]) #Ingles

            ####################################################################
            ####################################################################
            preguntas.append(

                 {
                    "count": 0,
                    "data": [{
                    "text": dat["Pregunta"],
                    "userDefined": True
                    }]
                }

            ) #Espanhol

            '''preguntas.append(

                 {
                    "count": 0,
                    "data": [{
                    "text": dat["Pregunta_en"],
                    "userDefined": True
                    }]
                }

            ) #Ingles'''
            ####################################################################
            
        except KeyError as err:

            pass

    #Payload ES
    #payload = { "contexts": [ " " ], "events": [], "fallbackIntent": False, "name": str(cat), "priority": 500000,  "responses": [ { "action": "add.list", "defaultResponsePlatforms": { "google": True }, "messages": [ { "platform": "google", "textToSpeech": "z", "type": "simple_response"},{ "speech": respuestas, "type": 0 } ], "parameters": [ { "dataType": "0", "isList": True, "name": "0", "prompts": [  " li " ], "required": True,  "value": "0" } ], "resetContexts": False } ],  "templates": [ "c:c ",    "b:b ", "a:a " ],  "userSays": preguntas,  "webhookForSlotFilling": False,  "webhookUsed": False} #JSON File
    
    #Payload EN
    payload = { "contexts": [ " " ], "events": [], "fallbackIntent": False, "name": str(cat), "priority": 500000,  "responses": [ { "action": "add.list", "defaultResponsePlatforms": { "google": True }, "messages": [ { "platform": "google", "textToSpeech": "z", "type": "simple_response"},{ "speech": respuestas, "type": 0 } ], "parameters": [ { "dataType": "0", "isList": True, "name": "0", "prompts": [  " li " ], "required": True,  "value": "0" } ], "resetContexts": False } ],  "templates": [ "c:c ",    "b:b ", "a:a " ],  "userSays": preguntas,  "webhookForSlotFilling": False,  "webhookUsed": False} #JSON File

    query_post = requests.post(

    'https://api.dialogflow.com/v1/intents?v=20150910', 
    headers = {'Authorization':'Bearer af8f01865f994a5186d4ae0b0b250d11', 'Content-Type':'application/json'},
    data = str(payload) 
    
    )

    print( query_post.text )

#print( query_get.text )

