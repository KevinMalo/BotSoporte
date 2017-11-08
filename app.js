var express = require('express');
var app = express();
var path    = require("path");

//app.use('/css', express.static(__dirname + '/css'));
//Store all JS and CSS in Scripts folder.

app.use(express.static('public'));



app.get('/', function (req, res) {
    
    res.sendFile(path.join(__dirname+'/index.html'));

});



app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
