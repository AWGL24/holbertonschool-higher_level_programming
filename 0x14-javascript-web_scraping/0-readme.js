#!/usr/bin/node
// Write a script that reads and prints the content of a file.

let fs = require('fs');
let file = process.argv[2];
let data = fs.readFileSync(file, 'utf8');
fs.readFile(file, function (err, data) {
	if (err) return console.error(err);
	console.log(data.toString());
});