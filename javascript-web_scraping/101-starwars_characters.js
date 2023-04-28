#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  const charactersCount = characters.length;
  let charactersLoaded = 0;
  let characterNames = new Array(charactersCount);
  characters.forEach(function (characterUrl, index) {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      characterNames[index] = JSON.parse(body).name;

      charactersLoaded++;
      if (charactersLoaded === charactersCount) {
        characterNames.forEach(function (name) {
          console.log(name);
        });
      }
    });
  });
});
