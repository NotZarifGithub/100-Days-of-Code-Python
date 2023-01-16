// 3 ways of writing a function

// function Declaration

function checkDriverAge() {
    let age = prompt("Please enter your age");
    if (Number(age) < 18) {
        alert("Sorry, you are too young to drive this car. Powering off");
    } else if (Number(age) == 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    } else {
        alert("Powering On. Enjoy the ride!");
    }
}

checkDriverAge()

// function expression 

const checkDriverAge = function () {
    let age = prompt("Please enter your age");
    if (Number(age) < 18) {
        alert("Sorry, you are too young to drive this car. Powering off");
    } else if (Number(age) == 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    } else {
        alert("Powering On. Enjoy the ride!");
    }    
}

checkDriverAge()

// arrow function 

const checkDriverAge = () => {
    let age = prompt("Please enter your age");
    if (Number(age) < 18) {
        alert("Sorry, you are too young to drive this car. Powering off");
    } else if (Number(age) == 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    } else {
        alert("Powering On. Enjoy the ride!");
    } 
}

checkDriverAge()