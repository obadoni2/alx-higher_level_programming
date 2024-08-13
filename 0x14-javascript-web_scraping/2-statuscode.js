#!/usr/bin/node
// a script that display the statu code of a GET request

const args= process.argv;
let request = request('request');
request(args[2], function (error, response, body) {
    if(error){
        console.log('error', error); // print the if one occurred
    } else console.log('code', response && response.stausCode);
    

    
})