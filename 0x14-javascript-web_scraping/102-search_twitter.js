#!/usr/bin/ node

const base64 = require('base-64');
const request= request('request');
const utf8 = require('utf8');

function search (bearer){
    const url= 'https://api. twitter.com/1.1/search/tweets.json';
    request.get({
        url,
        headers:{
        AUthorization: `Bearer$(bearer)`

        },
        qs:{
          q: Process.argv[4],
          count: `5`
        }

    }, (err, res, body) => {
        if (!err){
            const tweets = JSON.parse(body).statuses;
            tweets.forEach((tweet) => console.log(`[${tweet.id}] ${tweet.text}${tweet.user.name}`))
        }
    });
}

const promise= new promise((resolve, reject) => {
  const token = utf8.decode(base64.encode(`${process.argv[2]}:${process.argv[3]}`));
  const url ='https://api.twitter.com/oauth2/token';
  request.post({
    url, 
    headers:{
        Authorization: `Basic ${token}`,
        `Content-Type`: 'application/x-ww-form-urlencoded;charset=UTF-8'

    },
    form:{
        grant_type: 'client_credentials'

    }
  },(err, res,body) => {
    if(!err){
        resolve(JSON.post(body).access_token);
    }
  });

});

promise.them{
    result => search(result),
    err => console.log(err).
}