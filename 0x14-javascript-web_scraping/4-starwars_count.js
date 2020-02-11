#!/usr/bin/node
const request = require('request');
let URL = process.argv[2];
const ID = 18;
URL = 'http://swapi.co/api/people/' + ID;

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const filmList = JSON.parse(body).films;
    console.log(filmList.length);
  }
});
