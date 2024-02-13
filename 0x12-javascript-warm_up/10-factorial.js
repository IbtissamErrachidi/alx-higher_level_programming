#!/usr/bin/node
const first = process.argv[2];
const number = parseInt(first);
function factorial (num) {
  if (num === 0 || isNaN(num)) return 1;
  return num * factorial(num - 1);
}
console.log(factorial(number));
