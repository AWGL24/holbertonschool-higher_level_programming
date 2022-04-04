#!/usr/bin/node
// Script that searches the second biggest integer in the list of args

const args = process.argv.slice(2).map(Number);
let Bigsecond = 0;
if (args.lenght > 1) {
  Bigsecond = args.sort((a, b) => (b - a))[1];
}
console.log(Bigsecond);
