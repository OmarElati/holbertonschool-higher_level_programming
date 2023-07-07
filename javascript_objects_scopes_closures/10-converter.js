#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (number < base) {
      return number.toString();
    } else {
      return exports.converter(base)(Math.floor(number / base)) + (number % base < 10 ? (number % base).toString() : String.fromCharCode(55 + (number % base)));
    }
  };
};
