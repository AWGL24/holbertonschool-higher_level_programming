#!/usr/bin/node
// Script that displays the status code of a GET request

const https = require('https');
const URL = process.argv[2];
https.get(URL, function (res) {
	console.log('code:', res.statusCode);
});