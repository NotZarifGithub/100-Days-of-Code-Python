// Array of fruits

let array = ["Banana", "Apples", "Oranges", "Blueberries"];

// remove the "banana" from the array

array.shift();

console.log(array);

// sort the array in order 

array.sort();

console.log(array);

// Put "Kiwi" at t he end of the array

array.push("Kiwi");

console.log(array);

// Remove "Apples" from the array

array.splice(0, 1);

console.log(array);

// Sort the array in reverse order 

array.reverse();

console.log(array);

// using this array,
let array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// access "Oranges".

console.log(array2[1][1][0]);