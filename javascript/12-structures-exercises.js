// 1. Crea un array que almacene cinco animales
let animal = ["perro","gato","loro","dinosaurio","gallina"];
console.log(animal);

// 2. Añade dos más. Uno al principio y otro al final
animal.unshift("dragon");
animal.push("ultimo");
console.log(animal);

// 3. Elimina el que se encuentra en tercera posición
animal.splice(2,1); // posicion 2, elimina 1 elemento
console.log(animal);

// 4. Crea un set que almacene cinco libros
let libros = new Set();
libros.add("El principito");
libros.add("Don Quijote de la Mancha");
libros.add("La Odisea");
libros.add("Romeo y Julieta");
libros.add("Caperucita Roja");

console.log(libros);

// 5. Añade dos más. Uno de ellos repetido
libros.add("Constitución Española");
libros.add("La Odisea");

console.log(libros);

// 6. Elimina uno concreto a tu elección
libros.delete("Caperucita Roja");

console.log(libros);

// 7. Crea un mapa que asocie el número del mes a su nombre
meses = new Map([
	[1,"Enero"],
	[2,"Febrero"],
	[3,"Marzo"],
	[4,"Abril"],
	[5,"Mayo"],
	[6,"Junio"],
	[7,"Julio"],
	[8,"Agosto"],
	[9,"Septiembre"],
	[10,"Octubre"],
	[11,"Noviembre"],
	[12,"Diciembre"]
]);

console.log(meses);
console.log(meses.get(4));

// 8. Comprueba si el mes número 5 existe en el map e imprime su valor
console.log(meses.has(5));
console.log(meses.get(5));

// 9. Añade al mapa una clave con un array que almacene los meses de verano
meses.set("Verano", ["Junio", "Julio", "Agosto"]);

console.log(meses);

// 10. Crea un Array, transfórmalo a un Set y almacénalo en un Map
let datos = ["Cristian", "Jimenez", "Sanchez", "sajicri", 30, 666777888, "Avenida de la Constitución, 1"];
let datosSet = new Set(datos);
let datosMap = new Map();
datosMap.set("DatosPersonales", datosSet);

console.log(datosMap);