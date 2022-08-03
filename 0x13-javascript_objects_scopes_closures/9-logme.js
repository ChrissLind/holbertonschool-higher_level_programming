#!/usr/bin/node
let count = 0;
exports.logMe = item => console.log(`${count++}: ${item}`);
