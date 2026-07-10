// if/else/else if/ternaria

// 1. Imprime por consola tu nombre si una variable toma su valor
let x = 2
if (x == 2){
    console.log("Bienvenido Cristian")
}

// 2. Imprime por consola un mensaje si el usuario y contraseña concide con unos establecidos
let user = "admin"
let password = "admin1"

if(user === "admin" && password === "admin1"){
    console.log("Bienvenido Admin!")
}

// 3. Verifica si un número es positivo, negativo o cero e imprime un mensaje
let num = 7;

if (num !== 0){
	if (num > 0){
		console.log("EL numero es positivo");
	}
	else{
		console.log("El numero es negativo");
	}
}
else{
	console.log("El numero es 0");
}

// 4. Verifica si una persona puede votar o no (mayor o igual a 18) e indica cuántos años le faltan
let edad = 16;
let edadVoto = 18;
let añosRestantes = edadVoto - edad;

if (edad < 18){
	console.log(`No puede votar te faltan ${añosRestantes} años`);
}
else{
	console.log("Puede votar");
}
// 5. Usa el operador ternario para asignar el valor "adulto" o "menor" a una variable
//    dependiendo de la edad 

// 6. Muestra en que estación del año nos encontramos dependiendo del valor de una variable "mes"

// 7. Muestra el número de días que tiene un mes dependiendo de la variable del ejercicio anterior

// switch

// 8. Usa un switch para imprimir un mensaje de saludo diferente dependiendo del idioma

// 9. Usa un switch para hacer de nuevo el ejercicio 6

// 10. Usa un switch para hacer de nuevo el ejercicio 7