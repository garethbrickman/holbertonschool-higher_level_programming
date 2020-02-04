#!/usr/bin/node
const args2 = parseInt(process.argv[2]);
let print = '';
let i, j;

if (Number.isInteger(args2) !== true) {
  console.log('Missing size');
} else {
  for (i = 0; i < args2; i++) {
    print = '';
    for (j = 0; j < args2; j++) {
      print += 'X';
    }
    console.log(print);
  }
}
