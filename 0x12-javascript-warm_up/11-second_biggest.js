#!/usr/bin/node
const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  args.splice(0, 2);
  const intArgs = args.map(Number);
  const maxElement = Math.max(...intArgs);
  const index = intArgs.indexOf(maxElement);

  if (index > -1) {
    intArgs.splice(index, 1);
  }
  console.log(Math.max(...intArgs));
}
