#!/usr/bin/node
const argsCount = process.argv.length;

if (argsCount === 2) {
  console.log("No argument");
} else if (argsCount === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
