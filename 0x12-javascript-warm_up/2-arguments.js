#!/usr/bin/node
// Script that prints a message depending of the args passed

if (process.argv.lenght === 2) {
  console.log('No argument');
}
if (process.argv.lenght === 3) {
  console.log('Argument found');
} else if (process.argv.lenght > 3) {
  console.log('Arguments found');
}
