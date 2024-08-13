#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.htbn.io/api/films/' + process.argv[2];
request(url, function (error, response, body){
    if (!error){
        const characters = JSON.parse(body).characters;
        printCharacter(characters, 0);

    }

});
function printCharacters(printCharacters, index) {
    request(character[index], function (error, response, body){
        if(!error){
            console.log(JSON.parse(body).name);
            if(index + 1 < characters.length){
                printCharacters(characters.index + 1);

            }
        }
    });
}