
function getCarHonda(carInventory) {
    const hondaCar = carInventory.find(car => car.car_make === "Honda");

    if (hondaCar) {
        return `This is a ${hondaCar.car_make} ${hondaCar.car_model} from ${hondaCar.car_year}.`;
    } else {
        return "No Honda car found in the inventory.";
    }
}

const inventoryPartI = [
    { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
    { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
    { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
    { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
    { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

console.log(getCarHonda(inventoryPartI));

// Part II
function sortCarInventoryByYear(carInventory) {
    const sortedInventory = [...carInventory].sort((a, b) => a.car_year - b.car_year);
    return sortedInventory;
}

const inventoryPartII = [
    { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
    { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
    { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
    { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
    { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

console.log(sortCarInventoryByYear(inventoryPartII));
