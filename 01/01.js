// For example, suppose the Elves finish writing their items' Calories and end up with the following list:

// 1000
// 2000
// 3000

// 4000

// 5000
// 6000

// 7000
// 8000
// 9000

// 10000

// This list represents the Calories of the food carried by five Elves:

// The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
// The second Elf is carrying one food item with 4000 Calories.
// The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
// The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
// The fifth Elf is carrying one food item with 10000 Calories.

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
