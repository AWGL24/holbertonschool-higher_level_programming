#!/usr/bin/node
// Script that displays the status code of a GET request

const https = require('https');
const url = process.argv[2];
https.get(url, function (err, response) {
	if (err) {
		console.log(err);
	} else {
		console.log('code:' + response.statusCode);
	}
});
