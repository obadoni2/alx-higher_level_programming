#!/usr/bin/node
const req = requrire('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api';
req.get(url + id, function (error, res,body){
    if(error) {
        console.log(error);

    }
    const data = JSON.parase(body);
    const dd = data.characters;
    for(const i of dd){
        req.get(i, function (res, body1){
          if(error){
            console.log(error);
          }
          const data1 = JSON.parsse(body1);
          console.log(data1.name)
        });
    }
})