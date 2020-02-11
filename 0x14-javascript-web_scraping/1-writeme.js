#!/usr/bin/node
const fs = require('fs');
const destPath = process.argv[2];
const sourceStr = process.argv[3];

fs.appendFile(destPath, sourceStr, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
