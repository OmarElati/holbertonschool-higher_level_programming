#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${movieId}/`, (error, response, body) => {
  if (error) console.error(error);

  const charactersUrls = JSON.parse(body).characters;
  charactersUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) console.error(error);

      const characterName = JSON.parse(body).name;
      console.log(characterName);
    });
  });
});
