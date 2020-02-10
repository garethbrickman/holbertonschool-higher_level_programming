#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    // won't set attrs if w or h aren't +ve ints > 0
    if (Number.isInteger(w) !== true || w <= 0 ||
 Number.isInteger(h) !== true || h <= 0) {
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
