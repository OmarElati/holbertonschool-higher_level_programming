#!/usr/bin/node

function factorial(n) {
    if (isNaN(n)) {
      return 1;
    } else if (n <= 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  
  const arg = process.argv[2];
  console.log(factorial(parseInt(arg)));
  