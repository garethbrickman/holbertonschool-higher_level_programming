#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request
  .get(URL)
  .on('response', function (response) {
    console.log('code:', response && response.statusCode);
  });
