var express = require('express');
var app = express();
var path    = require("path");

//npm install unirest para hacer las peticiones GET y POST
var unirest = require('unirest');

//npm install body-parser para obtener los datos desde el html
var bodyParser = require('body-parser');

//Carga de archivos estaticos de la carpeta Public

app.use(express.static('public'));

//Ruta y render de nuestro archivo HTML
app.get('/', function (req, res) {
    
    res.sendFile(path.join(__dirname+'/index.html'));

});

app.get('/formulario', function (req, res) {
    
    res.sendFile(path.join(__dirname+'/formulario.html'));

});

////// BodyParse

//extended: false significa que parsea solo string (no archivos de imagenes por ejemplo)
app.use(bodyParser.urlencoded({ extended: false }));


var categoria = ""

var respuestas = []

var preguntas = []

app.post('/formulario', function (req, res) {
    
    categoria = req.body.categoria;

    respuestas.push(req.body.pregunta);
    
    preguntas.push(
        {
            "count": 0,
            "data": [{
            "text": req.body.respuesta,
            "userDefined": true
            }]
        }
    )

    console.log(categoria)
    console.log(preguntas)
    console.log(respuestas)

    var payload = {"contexts":[""],"events":[],"fallbackIntent":false,"name":categoria,"priority":500000,"responses":[{"action":"add.list","affectedContexts":[],"defaultResponsePlatforms":{"google":true},"messages":[{"platform":"google","textToSpeech":"Okay","type":"simple_response"},{"speech":respuestas,"type":0}],"parameters":[{"dataType":"0","isList":true,"name":"0","prompts":["li"],"required":true,"value":"0"}],"resetContexts":false}],"templates":["c:c ","b:b ","a:a "],"userSays":preguntas,"webhookForSlotFilling":false,"webhookUsed":false}
    
    //Unirest: Peticion POST a la API de DialogFlow
    unirest.post('https://api.dialogflow.com/v1/intents?v=20150910')
    .headers({
        'Authorization':'Bearer af8f01865f994a5186d4ae0b0b250d11', 
        'Content-Type':'application/json'
    })
    .send(payload)
    .end(function (response) {
      console.log(response.body);
    });

    res.redirect('/formulario');

})

//////

app.listen(3000, function () {
  console.log('App funcionando en el puerto 3000!');
});
