#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print() {
    let row = "";
    for (let i = 0; i < this.width; i++) {
      row += "X";
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
