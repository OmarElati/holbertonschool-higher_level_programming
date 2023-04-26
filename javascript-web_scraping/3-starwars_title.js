#!/usr/bin/node
const request = require('request');
const args = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(args[0]);

request(url, (error, _response, body) => {
  if (error) {
    console.error(error);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
