#!/usr/bin/node
// starswar api task to get movie characters by id

const request = require('request');
const movieId = process.argv[2];

function getMovieCharacters (characters, idx) {
  if (idx === characters.length) return;

  request(characters[idx], function (error, response, body) {
    if (error || response.statusCode !== 200) {
      console.error(`Failed to retrive data for movie ID ${movieId}:`, error);
    } else {
      console.log(JSON.parse(body).name);
      getMovieCharacters(characters, idx + 1);
    }
  });
}

const apiurl = `https://swapi.dev/api/films/${movieId}/`;
request(apiurl, function (err, response, body) {
  if (err || response.statusCode !== 200) {
    console.error(`Error fetching movie with that ID ${movieId}`, err);
  } else {
    const characters = JSON.parse(body).characters;
    getMovieCharacters(characters, 0);
  }
});
