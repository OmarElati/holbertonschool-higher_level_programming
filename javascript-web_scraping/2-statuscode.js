#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
