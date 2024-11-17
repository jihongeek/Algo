let inputStringArray = require('fs').readFileSync(0).toString().split('\n');
const choPieceArray:Int32Array = inputStringArray[0].split(' ').map((x:string)=> parseInt(x)); 
const hanPieceArray:Int32Array = inputStringArray[1].split(' ').map((x:string)=> parseInt(x));

const pointMappingArray = [13,7,5,3,3,2];
let choScore = 0;
let hanScore = 1.5;

choPieceArray.forEach((x,index) => {
    choScore += pointMappingArray[index]*x;
});
hanPieceArray.forEach((x,index) => {
    hanScore += pointMappingArray[index]*x;
});

if (choScore > hanScore) {
    console.log('cocjr0208');
} else {
    console.log('ekwoo');
}