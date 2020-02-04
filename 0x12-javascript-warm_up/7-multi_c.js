#!/usr/bin/node
const args2 = parseInt(process.argv[2]);
const c = 'C is fun';
let i;

if (Number.isInteger(args2) !== true) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < args2; i++) {
    console.log(c);
  }
}
