#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    return number === 0 ? '0' : (number < base ? '' : exports.converter(base)(Math.floor(number / base))) + (number % base < 10 ? (number % base).toString() : String.fromCharCode(87 + (number % base)));
  };
};
