#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (number === 0) {
      return '';
    } else {
      const remainder = number % base;
      const quotient = Math.floor(number / base);
      const converted = exports.converter(base)(quotient);
      const digit = remainder < 10 ? remainder.toString() : String.fromCharCode(55 + remainder);
      return converted + digit;
    }
  };
};
