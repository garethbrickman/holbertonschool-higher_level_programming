#!/usr/bin/node
const oldSquare = require('./5-square');
class Square extends oldSquare {
  charPrint (c) {
    if (c === undefined) {
      const character = 'C';
      let print = '';
      for (let i = 0; i < this.height; i++) {
        print = '';
        for (let j = 0; j < this.width; j++) {
          print += character;
        }
        console.log(print);
      }
    } else {
      const character = 'X';
      let print = '';
      for (let i = 0; i < this.height; i++) {
        print = '';
        for (let j = 0; j < this.width; j++) {
          print += character;
        }
        console.log(print);
      }
    }
  }
}
module.exports = Square;
