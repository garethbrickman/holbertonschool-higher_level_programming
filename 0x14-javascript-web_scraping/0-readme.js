#!/usr/bin/node
const fs = require('fs');
const sourcePath1 = process.argv[2];

fs.readFile(sourcePath1, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
