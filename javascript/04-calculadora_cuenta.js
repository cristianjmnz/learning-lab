const readlineSync = require('readline-sync');

let data = [];

// Pedir los datos al cliente
data[0] = readlineSync.question("Indique el total de la cuenta: ");
data[1] = readlineSync.question("Indique la cantidad de propina si lo desea: ");
data[2] = readlineSync.question("Indique el numero de personas que son: ");

// Variables necesarias
let cuenta = parseFloat(data[0]);
let porcentaje = parseFloat(data[1]);
let numPersonas = parseInt(data[2]);

// Bienvenida
console.log("-----Calculadora de cuenta del restaurante-----");

// Calcular la propina
let propina = (porcentaje/100) * cuenta;

// Calcular el total
let total = cuenta + propina;

// Calcular la cantidad por persona
let cantidadPorPersona = total / numPersonas;

// Mostrar los resultados
console.log(`Total (incluido propina): $${total}`);
console.log(`Cantidad por persona: $${cantidadPorPersona}`);