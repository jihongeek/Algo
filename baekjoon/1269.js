const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

/*
    대칭차집합 
    A-B => A에만 있고 B에는 없는 원소
    B-A => B에만 있고 A에는 없는 원소
    ==> 각각 A,B에만 있는 원소의 갯수 
    
*/

let setA = {};
let setB = {};
let count = 0;

const [numberOfSetA,numberOfSetB] = input[0]; 
for (let element of input[1].split(" ") ) 
{
    setA[element] = true;
}
for (let element of input[2].split(" ") ) 
{
    setB[element] = true;
}
for (let setNumber = 1; setNumber <= 2; setNumber++)
{
    for (let element of input[setNumber].split(" "))
    {
        if (setNumber === 1 && setA[element] === true && setB[element] === undefined)
        {
            count++;
        }
        if (setNumber === 2 && setA[element] === undefined && setB[element] === true)
        {
            count++;
        }          
    }        
}
console.log(count);