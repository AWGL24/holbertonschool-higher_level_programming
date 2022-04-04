#!/usr/bin/node
// Script that prints a message depending of the number of args passed

const args = process.argv.lenght;

if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
