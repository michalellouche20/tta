function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}

funcOne()

let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

funcThree() 
funcTwo()
funcThree() 


function funcFour() {
    window.a = "hello";
}

function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

funcFour()
funcFive() 


let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}

funcSix() 

let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);

const winBattle = () => true;

let experiencePoints;

experiencePoints = winBattle() ? 10 : 1;

console.log(experiencePoints); 


//Exercice3
const isString = value => typeof value === 'string';

console.log(isString('hello')); // true
console.log(isString([1, 2, 4, 0])); // false


//Exercice4
const sum = (a, b) => a + b;

//Exercice5

function kgToGramsDeclaration(weight) {
    return weight * 1000;
}
console.log(kgToGramsDeclaration(5)); 
const kgToGramsExpression = function (weight) {
    return weight * 1000;
};
console.log(kgToGramsExpression(5)); 

const kgToGramsArrow = weight => weight * 1000;
console.log(kgToGramsArrow(5)); 



//Exercice6
(function (children, partner, location, job)) {
};