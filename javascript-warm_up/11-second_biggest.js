#!/usr/bin/node
const args = process.argv.slice(2);
const arr = args.map(arg => parseInt(arg));

if (arr.length <= 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      secondMax = max;
      max = arr[i];
    } else if (arr[i] > secondMax && arr[i] < max) {
      secondMax = arr[i];
    }
  }

  console.log(secondMax);
}
