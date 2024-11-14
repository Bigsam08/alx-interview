#!/usr/bin/node
// starswar api task to get movie characters by id

const request = require('request');
const movieId = process.argv[2];
const apiurl = `https://swapi.dev/api/films/${movieId}/`;

function getMovieCharacters (movieId) {
  request(apiurl, { json: true }, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error(`Failed to retrive data for movie ID ${movieId}`);
      return;
    }
    const charURLs = body.characters;

    charURLs.forEach((charURL) => {
      request(charURL, { json: true }, (CharErr, charRes, charbody) => {
        if (CharErr || charRes.statusCode !== 200) {
          console.error(`Failed to retrive character at ${charURLs}`);
          return;
        }
        console.log(charbody.name);
      });
    });
  });
}

if (!movieId) {
  console.log('invalid Usage!! Usage: ./0-starwars_characters.js < movie id >');
} else {
  getMovieCharacters(movieId);
}
