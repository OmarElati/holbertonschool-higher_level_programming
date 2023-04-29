#!/usr/bin/node
class Rectangle {
  constructor (w = 0, h = 0) {
    if (w <= 0 || h <= 0) {
      // empty rectangle
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
