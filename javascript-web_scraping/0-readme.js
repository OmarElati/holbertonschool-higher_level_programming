#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

fs.readFile(args[0], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
