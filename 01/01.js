// Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? (24000)

let sourceText = `1000
2000
3000

4000

5000
6000

7000
8000
9000

10000`;

let itemList = sourceText.split('\n');
let myElves = [];
let currentCals = 0;

for (const num of itemList) {
    if (num == '') {
        myElves.push(currentCals);
        currentCals = 0;
    } else {
        currentCals += parseInt(num);
    }
}

console.log(myElves);