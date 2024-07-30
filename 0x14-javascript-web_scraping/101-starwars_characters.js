#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
let chars = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  chars = data.characters;
  findGlobalChars(0);
});

const findGlobalChars = (index) => {
  if (index === chars.length) {
    return;
  }

  request(chars[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    findGlobalChars(index + 1);
  });
};
