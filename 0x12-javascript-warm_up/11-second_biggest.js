#!/usr/bin/node
const args = process.argv;
let copyArray = [];
let compArray = [];
let newArray = [];

if (args.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    copyArray += args[i];
    compArray += args[i];
  }
  for (let i = 0; i < copyArray.length; i++) {
    if (copyArray[i] > compArray[i + 1]) {
      newArray += copyArray[i];
    }
  }
  console.log(newArray[0]);
}
