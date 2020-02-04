#!/usr/bin/node
const x = parseInt(process.argv[2]);

if (Number.isInteger(x) !== true) {
  console.log(1);
} else {
  console.log(factorial(x));
}

function factorial (x) {
  return (x !== 1) ? x * factorial(x - 1) : 1;
}
