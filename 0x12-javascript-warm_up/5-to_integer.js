#!/usr/bin/node
const args2 = parseInt(process.argv[2]);
if (Number.isInteger(args2) === true) {
  console.log(`My number is: ${args2}`);
} else {
  console.log('Not a number');
}
