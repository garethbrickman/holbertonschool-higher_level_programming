#!/usr/bin/node
const fs = require('fs');
const endOfLine = require('os').EOL;
const sourcePath1 = process.argv[2];
const sourcePath2 = process.argv[3];
const destPath = process.argv[4];

const content1 = fs.readFileSync(sourcePath1, 'utf8');
const content2 = fs.readFileSync(sourcePath2, 'utf8');

const writer = fs.createWriteStream(destPath, {
  flags: 'a'
});
writer.write(content1);
writer.write(endOfLine);
writer.write(content2);
writer.end();
