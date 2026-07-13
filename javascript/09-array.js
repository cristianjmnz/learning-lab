// Array

// Declaración

let myArray = [];
let myArray2 = new Array();

console.log(myArray);
console.log(myArray2);

// Inicialización

myArray = [3];
myArray2 = new Array(4);

console.log(myArray);
console.log(myArray2);

myArray = ["Cristian", "Sajicri", "cristiandev", 30, true];
myArray2 = new Array("Cristian", "Sajicri", "cristiandev", 30, true);

console.log(myArray);
console.log(myArray2);

myArray2 = new Array(3);
myArray2[2] = "Cristian";

console.log(myArray2);

// Métodos comunes

myArray = []

// push y pop
// push agrega un elemento al final del array
myArray.push("Hola");
myArray.push("Javascript");
myArray.push("pokemón");
myArray.push(33);

console.log(myArray)

// pop elimina el último elemento del array y te lo muestra
console.log(myArray.pop());
myArray.pop();

console.log(myArray);

// shift y unshift

console.log(myArray.shift()); // Elimina el primer elemento del array y te lo muestra
console.log(myArray);

myArray.unshift("Brais", "mouredev"); // Añade elementos al inicio del array
console.log(myArray);

// length

console.log(myArray.length);

// clear
// Forma de vaciar un array
myArray = [];
myArray.length = 0; // alternativa
console.log(myArray);

// slice
// slice crea un nuevo array a partir de un array existente
myArray = ["Cristian", "Sajiri", "cristiandev", 30, true];

let myNewArray = myArray.slice(1, 3);

console.log(myArray);
console.log(myNewArray);

// splice
// splice elimina elementos de un array y opcionalmente añade nuevos elementos
myArray.splice(1, 3);
console.log(myArray);

myArray = ["Cristian", "Sajiri", "cristiandev", 30, true];

myArray.splice(1, 2, "Nueva entrada");
console.log(myArray);