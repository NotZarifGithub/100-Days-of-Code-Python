var firtsName = "Muhammad Zarif";
var lastName = "Abd Raman"

var myName = firtsName + " bin " + lastName;

if (firtsName === "Muhammad Zarif") {
    alert(firtsName + " you're cool")
} else if (lastName === "Abd Raman") {
    alert(lastName + " you're cool")    
} else {
    prompt("What's your name?")
}

if (firtsName === "Muhammad Zarif" && lastName === "Abd Raman") {
    alert(myName + " you're cool");
} else if (firtsName == "Muhammad Zarif") {
    alert(firtsName + " you're cool");
} else if (lastName === "Abd Raman") {
    alert(lastName + " you're cool");
} else {
    alert("I'm sorry, I do not know you")
}

var operator = prompt("Do you want to add subtract multiply of divide")
var firstNumber = prompt("What's the first number");
var secondNumber = prompt("What's the second number");

if (operator === "add") {
    alert(Number(firstNumber) + Number(secondNumber));
} else if (operator === "subtract") {
    alert(Number(firstNumber) - Number(secondNumber));
} else if (operator === "multiply") {
    alert(Number(firstNumber) * Number(secondNumber));
} else if (operator === "divide") {
    alert(Number(firstNumber) / Number(secondNumber));
}

function multiply(a, b) {
    return console.log(a * b);
}

multiply(10, 4)

var listOfAnimals = ["cat", "dog", "beaver", "fish", "ape"];

console.log(listOfAnimals.sort())

const multiply = (a, b) => {
    return console.log(a * b)
}