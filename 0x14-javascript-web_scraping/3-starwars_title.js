#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const URL = 'http://swapi.co/api/films/' + movieID;

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
