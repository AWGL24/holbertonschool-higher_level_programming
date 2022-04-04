#!/usr/bin/node
// Script that prints x times "C is fun"

const count = process.argv[2];
if (isNaN(count)) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < x; i++) {
		console.log('C is fun');
	}
}
