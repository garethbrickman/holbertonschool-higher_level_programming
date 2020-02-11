#!/usr/bin/node
const fs = require('fs');
const sourcePath1 = process.argv[2];
const sourcePath2 = process.argv[3];
const destPath = process.argv[4];

// readFileSync(filepath, 'utf8') for plain text
const content1 = fs.readFileSync(sourcePath1);
const content2 = fs.readFileSync(sourcePath2);

const writer = fs.createWriteStream(destPath, {
  flags: 'a'
});
writer.write(content1);
// use this to insert blank line
// const endOfLine = require('os').EOL;
// writer.write(endOfLine);
writer.write(content2);
writer.end();
