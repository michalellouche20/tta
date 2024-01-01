//EX 1
function displayNumbersDivisible(divisor) {
    let sum = 0;

    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            console.log(i);
            sum += i;
        }
    }

    console.log(`Sum: ${sum}`);
}

displayNumbersDivisible(23);

//Ex 2
const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
};

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
};

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let total = 0;

    for (let item of shoppingList) {
        if (item in stock) {
            total += prices[item];
            stock[item] -= 1;
        }
    }

    return total;
}

console.log(`Total Price: $${myBill()}`);

//Ex 3
function changeEnough(itemPrice, amountOfChange) {
    const sumOfChange = amountOfChange[0] * 0.25 + amountOfChange[1] * 0.10 + amountOfChange[2] * 0.05 + amountOfChange[3] * 0.01;

    return sumOfChange >= itemPrice;
}

//Ex 4
function hotelCost() {
    let numberOfNights;

    do {
        numberOfNights = prompt("Enter the number of nights you would like to stay in the hotel:");
    } while (isNaN(numberOfNights) || numberOfNights === null);

    return numberOfNights * 140;
}

function planeRideCost() {
    let destination;

    do {
        destination = prompt("Enter your destination (London, Paris, or any other destination):").toLowerCase();
    } while (!destination || (destination !== "london" && destination !== "paris"));

    switch (destination) {
        case "london":
            return 183;
        case "paris":
            return 220;
        default:
            return 300;
    }
}

function rentalCarCost() {
    let numberOfDays;

    do {
        numberOfDays = prompt("Enter the number of days you would like to rent the car:");
    } while (isNaN(numberOfDays) || numberOfDays === null);

    let carCost = numberOfDays * 40;

    if (numberOfDays > 10) {
        carCost *= 0.95;
    }

    return carCost;
}

function totalVacationCost() {
    const hotelCostValue = hotelCost();
    const planeRideCostValue = planeRideCost();
    const rentalCarCostValue = rentalCarCost();

    const totalCost = hotelCostValue + planeRideCostValue + rentalCarCostValue;

    return totalCost;
}

console.log(`Total Vacation Cost: $${totalVacationCost()}`);

//Ex 5
const container = document.getElementById("container");
console.log(container);

const listItems = document.querySelectorAll("ul.list li");
listItems[1].textContent = "Richard";

const secondList = document.querySelectorAll("ul.list")[1];
secondList.removeChild(secondList.children[1]);
const yourName = "Your Name"; // Replace with your actual name

lists.forEach(list => {
    const firstListItem = list.querySelector("li");
    if (firstListItem) {
        firstListItem.textContent = 'michal';
    }
});

console.log(container.innerHTML);

const allLists = document.querySelectorAll("ul.list");
allLists.forEach(list => list.classList.add("student_list"));

allLists[0].classList.add("university", "attendance");

container.style.backgroundColor = "lightblue";
container.style.padding = "10px";

const danListItem = document.querySelector("li:contains('Dan')");
danListItem.style.display = "none";

listItems[1].style.border = "1px solid black";

document.body.style.fontSize = "18px";

 //Ex 6
const navBar = document.getElementById("socialNetworkNavigation");

const newListItem = document.createElement("li");
const textNode = document.createTextNode("Logout");
newListItem.appendChild(textNode);
navBar.querySelector("ul").appendChild(newListItem);

console.log(`First Link: ${navBar.querySelector("ul").firstElementChild.textContent}`);
console.log(`Last Link: ${navBar.querySelector("ul").lastElementChild.textContent}`);


//Ex 7
const allBooks = [
    {
        title: "Book 1",
        author: "Author 1",
        image: "url1",
        alreadyRead: true
    },
    {
        title: "Book 2",
        author: "Author 2",
        image: "url2",
        alreadyRead: false
    }
];

const listBooksSection = document.querySelector(".listBooks");

allBooks.forEach(book => {
    const bookDiv = document.createElement("div");
    
    const bookInfo = document.createTextNode(`${book.title} written by ${book.author}`);
    bookDiv.appendChild(bookInfo);

    const bookImage = document.createElement("img");
    bookImage.src = book.image;
    bookImage.style.width = "100px";
    bookDiv.appendChild(bookImage);

    if (book.alreadyRead) {
        bookDiv.style.color = "red";
    }

    listBooksSection.appendChild(bookDiv);
});
