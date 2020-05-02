var net = require('net');
var fs = require('fs');
var buffer = require('buffer');

var server = net.createServer(function(conn) {
    console.log('server connected');

    conn.on('data', function(data) {
        console.log('data received');
        console.log('data is: \n' + data);
    });
});

var HOST = '127.0.0.1';
var PORT = '9001'
var FILEPATH = '/home/steve/Downloads/';


server.listen(PORT, HOST, function() {
    //listening
    console.log('server bound to ' + PORT + '\n');

    server.on('connection', function(){
        console.log('connection made...\n')
    })
});