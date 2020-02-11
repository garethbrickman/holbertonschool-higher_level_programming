#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const destPath = process.argv[3];

// Makes API request, will print error object if occurs

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    // Takes results and deserializes from JSON to js obj
    // console.log(Object.prototype.toString.call(array)) to confirm obj type

    const obj = body;

    // writes obj to file
    fs.appendFile(destPath, obj, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
