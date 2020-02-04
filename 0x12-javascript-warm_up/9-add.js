#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];

console.log(add(a, b));

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
