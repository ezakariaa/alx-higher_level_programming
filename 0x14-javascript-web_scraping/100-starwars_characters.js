#!/usr/bin/node

const req = require('request');
const pathname = 'https://swapi-api.hbtn.io/api/films/';
const slug = process.argv[2];
req.get(pathname + slug, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const responseData = JSON.parse(body);
  const characters = responseData.characters;
  for (const i of characters) {
    req.get(i, function (error, res, chars) {
      if (error) {
        console.log(error);
      }
      const mydata = JSON.parse(chars);
      console.log(mydata.name);
    });
  }
});
