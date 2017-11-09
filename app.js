var express = require('express');
var app = express();
var path    = require("path");

var unirest = require('unirest');

var bodyParser = require('body-parser');

//app.use('/css', express.static(__dirname + '/css'));
//Store all JS and CSS in Scripts folder.

app.use(express.static('public'));



app.get('/', function (req, res) {
    
    res.sendFile(path.join(__dirname+'/index.html'));

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
    
    
    unirest.post('https://api.dialogflow.com/v1/intents?v=20150910')
    .headers({
        'Authorization':'Bearer af8f01865f994a5186d4ae0b0b250d11', 
        'Content-Type':'application/json'
    })
    .send(payload)
    .end(function (response) {
      console.log(response.body);
    });

})

//////









app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
