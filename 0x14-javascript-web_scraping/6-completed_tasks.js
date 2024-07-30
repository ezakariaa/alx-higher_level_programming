#!/usr/bin/node

const request = require('request');
const pathname = process.argv[2];

request(pathname, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const done = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const mytask = tasks[i];
      if (mytask.completed === true) {
        if (done[mytask.userId] === undefined) {
          done[mytask.userId] = 1;
        } else {
          done[mytask.userId]++;
        }
      }
    }
    console.log(done);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
