#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
let count = 0;

request(args[0], (error, response) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(response.body).results;
    for (const i in results) {
      const characters = results[i].characters;
      for (const i in characters) {
        if (characters[i].includes('18')) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
