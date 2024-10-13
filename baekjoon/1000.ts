import fs = require('fs')
const input = fs.readFileSync(0).toString().split(' ');
const a = parseInt(input[0]);
const b = parseInt(input[1]);
console.log(a+b);