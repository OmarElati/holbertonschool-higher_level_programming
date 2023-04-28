#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
const url = args[0];
const path = args[1];

request.get(url, (error, Response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(path, body, 'utf-8', error => {
      if (error) {
        return console.log(error);
      }
    });
  }
});
