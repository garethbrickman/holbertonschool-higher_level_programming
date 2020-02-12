#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

// Makes API request, will print error object if occurs

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    // Takes results and deserializes from JSON to js obj
    // console.log(Object.prototype.toString.call(array)) to confirm obj type

    const array = JSON.parse(body).results;

    // iterate through nested arrays to run the search, count hits
    let count = 0;
    for (let i = 0; i < array.length; i++) {
      for (let j = 0; j < array[i].characters.length; j++) {
        if (array[i].characters[j].indexOf('/18/') >= 0) { count += 1; }
      }
    }
    console.log(count);
  }
});
