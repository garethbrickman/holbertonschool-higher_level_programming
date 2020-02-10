#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) !== true || w <= 0 || Number.isInteger(h) !== true || h <= 0) {
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
