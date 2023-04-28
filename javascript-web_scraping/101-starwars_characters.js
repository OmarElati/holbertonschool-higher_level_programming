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
  characters.forEach(function (characterUrl) {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      const characterName = JSON.parse(body).name;
      console.log(characterName);
      charactersLoaded++;
      if (charactersLoaded === charactersCount) {
        // All characters loaded
      }
    });
  });
});
