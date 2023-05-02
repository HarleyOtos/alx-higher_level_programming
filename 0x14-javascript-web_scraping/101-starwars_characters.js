#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const charactersUrlList = JSON.parse(body).characters;
  const charactersList = [];

  let requestsLeft = charactersUrlList.length;

  charactersUrlList.forEach((characterUrl) => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }

      charactersList.push(JSON.parse(body).name);
      requestsLeft--;

      if (requestsLeft === 0) {
        // all requests have finished
        console.log(charactersList.join('\n'));
      }
    });
  });
});
