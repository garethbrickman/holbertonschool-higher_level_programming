#!/usr/bin/node
const oldSquare = require('./5-square');
class Square extends oldSquare {
  charPrint (c) {
    if (c) {
      let print = '';
      for (let i = 0; i < this.height; i++) {
        print = '';
        for (let j = 0; j < this.width; j++) {
          print += 'C';
        }
        console.log(print);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
