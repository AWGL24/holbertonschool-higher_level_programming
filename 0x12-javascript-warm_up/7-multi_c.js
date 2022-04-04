#!/usr/bin/node
// Script that prints x times "C is fun"

const count = process.argv[2];
let i = 0;

if (isNaN(count)) {
	console.log('Missing number of occurrences');
} else {
	for (; i < x; i++) {
		console.log('C is fun');
	}
}
