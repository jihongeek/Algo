const fs = require('fs');

const hidedPasswordDigits = fs.readFileSync(0).toString().split('\n').map((x)=>parseInt(x));

let decodedPassword = (hidedPasswordDigits[0] & 15) << 8;
decodedPassword |= (hidedPasswordDigits[1] & 15) << 4;   
decodedPassword |= (hidedPasswordDigits[2] & 15);

let passwordString = decodedPassword.toString();
console.log(passwordString.padStart(4,'0'));