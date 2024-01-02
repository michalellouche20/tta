//Ex 1
//output//
"I am John Doe from Vancouver , Canada. Latitude 49.2827 ,Longitude 123.1207";

//Ex 2
function displayStudentInfo(objUser) {
  const { first, last } = objUser;

  const fullName = `Your full name is ${first} ${last}`;

  return fullName;
}

const result = displayStudentInfo({ first: "Elie", last: "Schoppik" });
console.log(result);

//Ex 3
const users = { user1: 18273, user2: 92833, user3: 90315 };
const usersArray = Object.entries(users);
console.log(usersArray);
const modifiedArray = usersArray.map(([user, id]) => [user, id * 2]);
console.log(modifiedArray);

//Ex 4
//output = object//

//Ex 5
//right output is = 4

//Ex 6
1;
//For [2] === [2], you're comparing two different array objects, so it evaluates to false.

//For {} and {}, you're comparing two different objects, so it also evaluates to false.

2;
//the object 1,2,3 were 5 in the beggining and theve been modified to 4.
// theobject 5 didnt get modification and the numner of him will stay 5.

class Animal {
  constructor(name, type, color) {
    this.name = name;
    this.type = type;
    this.color = color;
  }
}

class Mammal extends Animal {
  sound(sound) {
    return `${sound} The ${this.type} named ${this.name} is ${this.color}`;
  }
}
const farmerCow = new Mammal("Lily", "cow", "brown and white");

console.log(farmerCow.sound("Moooo"));
