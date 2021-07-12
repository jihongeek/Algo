const readLine = require("readline");

const rl= readLine.createInterface({
  input: process.stdin,
  output:process.stdout
});

rl.on("line", function(line) {
    let n = parseInt(line);
    let count = 0
    for (let i = 3; i < n; i = i + 3) {
        for (let j = 3; j < n; j = j + 3) {
            console.log(i,j,n-i-j)
            if ((n - i - j) % 3 == 0 && n-i-j > 0) {
                count++;
            }
        }
    }
    console.log(count);
  	rl.close();
}).on("close", function() {
	process.exit();
})
