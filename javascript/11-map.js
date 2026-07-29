// Map

// Declaración

let myMap = new Map()

console.log(myMap)

// Inicialiación

myMap = new Map([
    ["name", "Cristian"],
    ["email", "cristianjmnz@gmail.com"],
    ["age", 30]
]);

console.log(myMap);

// Métodos y propiedades

// set

myMap.set("telefono", 666555777);
myMap.set("alias", "sajicri");

console.log(myMap);

// get --> te devuelve el valor de la clave que le pases como parámetro

console.log(myMap.get("name"));
console.log(myMap.get("surname"));
console.log(myMap.get("telefono"));

// has --> te devuelve true o false

console.log(myMap.has("surname"));
console.log(myMap.has("age"));

// delete --> elimina la clave que le pases como parámetro

myMap.delete("alias");
console.log(myMap);

// keys, values y entries

console.log(myMap.keys());
console.log(myMap.values());
console.log(myMap.entries());

// size

console.log(myMap.size);

// clear --> elimina todos los elementos del map

myMap.clear();
console.log(myMap);