#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    // Won't set attrs if w or h aren't +ve ints
    if (Number.isInteger(w) !== true || w <= 0 ||
Number.isInteger(h) !== true || h <= 0) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print Rectangle objs
  print () {
    let printer = '';
    for (let i = 0; i < this.height; i++) {
      printer = '';
      for (let j = 0; j < this.width; j++) {
        printer += 'X';
      }
      console.log(printer);
    }
  }

  // Method that swaps w & h
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // Method that doubles w & h
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
