const readLine = require("readline");

const rl= readLine.createInterface({
  input: process.stdin,
  output:process.stdout
});

function compare(user1,user2) {
    if (user1.age > user2.age) {
        return 1;
    }
    else if (user1.age < user2.age) {
        return -1;
    }
    if (user1.id > user2.id) {
        return 1;
    } 
    else if (user1.id < user2.id) {
        return -1;
    }
    return 0;
}

let users = [];
let testcase = null
let index = 0
rl.on("line", function(line) {
    
    if (testcase === null) {
        testcase = parseInt(line);
    }
    else {
        input = line.split(' ')
        users.push({id : index++, 
            age : parseInt(input[0]),
            username : input[1]
        });
    }
}).on("close", function() {
	users.sort(compare)
    for (let i = 0; i < users.length; i++) {
        console.log(users[i].age,users[i].username)
    }
    process.exit();
})