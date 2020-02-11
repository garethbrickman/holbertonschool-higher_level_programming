#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
Object.assign(newDict, dict);
console.log(newDict);
