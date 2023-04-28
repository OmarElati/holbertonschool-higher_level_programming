#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
const completedTasks = {};

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.forEach(task => {
      if (task.completed) {
        const userID = task.userId.toString();
        if (userID in completedTasks) {
          completedTasks[userID] += 1;
        } else {
          completedTasks[userID] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});
