#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const charactersUrls = JSON.parse(body).characters;
  const charactersList = [];

  let requestsLeft = charactersUrls.length;

  charactersUrls.forEach((charUrl) => {
    request(charUrl, (err, _response, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      const characterName = JSON.parse(charBody).name;
      charactersList.push(characterName);
      requestsLeft--;

      if (requestsLeft === 0) {
        console.log(charactersList.join('\n'));
      }
    });
  });
});
