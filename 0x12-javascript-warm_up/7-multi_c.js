#!/usr/bin/node
// Script that prints x times "C is fun"

let count = process.argv[2];
if (isNaN(count)) {
	console.log('Missing number of occurrences');
} else {
	for (; count > 0; count--) {
		console.log('C is fun');
	}
}
