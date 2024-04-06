#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const requestURL = `https://swapi-api.alx-tools.com/api/films/${id}`;

request({ url: requestURL, json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response && response.statusCode === 200) {
    console.log(body.title);
  }
});
