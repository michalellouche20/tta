const people = ["Greg", "Mary", "Devon", "James"];
console.log(people)
people.splice(0,1)
console.log(people)
people.splice(2,1,'Jason');
console.log(people)
people.push('Michal')
let MaryIndex = people.indexOf("Mary");
console.log(MaryIndex)
console.log(people.slice(0,-1));
console.log("Index of Foo:", people.indexOf("Foo"));
const last = people[people.length - 1];
console.log("Last Element:", last);

//Part 2

for (let person of people) {
    console.log(person);
}

    for (let person of people)
{
    console.log(person);
    if (person === "Devon") {
        break;
    }
}

const colors = ["blue", "red", "green", "yellow", "purple"];

for (let i = 0; i < colors.length; i++) {
  console.log(`My #${i + 1} choice is ${colors[i]}`);
}

const userInput = prompt("Enter a number:");

console.log(typeof userInput);
while (parseFloat(userInput) < 10);{
console.log('Write a new number')
}

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log("Number of Floors:", building.numberOfFloors);
console.log("Number of apt Floors:", building.numberOfAptByFloor.firstFloor);
console.log("Number of apt Floors:", building.numberOfAptByFloor.thirdFloor);

console.log('the name of the second tenant and the number of rooms :',building.nameOfTenants[1],building.numberOfRoomsAndRent.dan)

const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
    console.log("Dan's rent increased to 1200.");
}

console.log(building);

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  
let resultString = '';

for (const key in details) {
  resultString += details[key] + ' ';
}

console.log(resultString.trim());

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

console.log()