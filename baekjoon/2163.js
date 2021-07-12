const readLine = require("readline");

const rl= readLine.createInterface({
  input: process.stdin,
  output:process.stdout
});

rl.on("line", function(line) {
    let input = line.split(' ');
    let n = parseInt(input[0]);
    let m = parseInt(input[1]);
    console.log(n*m-1);
  	rl.close();
}).on("close", function() {
	process.exit();
})