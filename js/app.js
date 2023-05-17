const fs = require('fs');
const data = fs.readFileSync('./lib/timetable.json');
const json = JSON.parse(data);

const jsonString = JSON.stringify(json);

const http = require("http");
http.createServer(function(request,response){
     
    response.end(jsonString);
     
}).listen(3000,function(){
    console.log("Сервер начал прослушивание запросов на порту 3000");
});