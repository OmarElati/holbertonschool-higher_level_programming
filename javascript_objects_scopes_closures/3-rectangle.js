#!/usr/bin/node
class Rectangle {
  constructor (w = 0, h = 0) {
    if (w <= 0 || h <= 0) {
      // Return empty
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
