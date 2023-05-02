#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const url = `https://swapi-api.alx.tools/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const charactersUrls = JSON.parse(body).characters;
    charactersUrls.forEach(url => {
      request(url, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
