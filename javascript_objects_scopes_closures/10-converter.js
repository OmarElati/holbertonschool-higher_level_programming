#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (number === 0) {
      return '0';
    } else {
      let result = '';
      while (number > 0) {
        const digit = number % base;
        result = (digit < 10 ? digit : String.fromCharCode(87 + digit)) + result;
        number = Math.floor(number / base);
      }
      return result;
    }
  };
};
