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