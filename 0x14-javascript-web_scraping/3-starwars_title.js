#!/usr/bin/node
const request = require('request');

const filmIndex = process.argv[2];
const SWAPI_FILMS_URL = 'https://swapi-api.hbtn.io/api/films/';

request(SWAPI_FILMS_URL + filmIndex, function (error, httpResponse, responseBody) {
  if (error) {
    console.log(error);
  } else if (httpResponse.statusCode === 200) {
    const filmData = JSON.parse(responseBody);
    console.log(filmData.title);
  } else {
    console.log('Error code: ' + httpResponse.statusCode);
  }
});
