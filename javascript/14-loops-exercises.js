// NOTA: Explora diferentes sintaxis de bucles para resolver los ejercicios

// 1. Crea un bucle que imprima los números del 1 al 20
for (let i = 1; i <= 20; i++){
	console.log(i)
};

// 2. Crea un bucle que sume todos los números del 1 al 100 y muestre el resultado
let sumaTotal = 0;
for (let i = 1; i <= 100; i++){
    sumaTotal += i;
}
console.log(sumaTotal);

// 3. Crea un bucle que imprima todos los números pares entre 1 y 50
for (let num = 1; num <= 50; num++){
	if(num % 2 == 0){
        console.log(num);
    }
	
}

// 4. Dado un array de nombres, usa un bucle para imprimir cada nombre en la consola
name = ["Cristian","Susana","Freya","Jazmine"];

for(let i = 0; i < name.length; i++){
    console.log(name[i]);
	
}

// 5. Escribe un bucle que cuente el número de vocales en una cadena de texto
let texto = "Hola Cristian";
let contador = 0;

for (let i = 0; i < texto.length; i++){
    if ("aeiouAEIOU".includes(texto[i])){
        contador++;
    }
}

console.log(`Número de vocales: ${contador}`);

// 6. Dado un array de números, usa un bucle para multiplicar todos los números y mostrar el producto
let numeros = [1, 2, 3, 4, 5];
let producto = 1;
for (let i = 0; i < numeros.length; i++){
    producto *= numeros[i];
    console.log(producto);
}

// 7. Escribe un bucle que imprima la tabla de multiplicar del 5
for (let i = 1; i <= 10; i++){
    console.log(`5 x ${i} = ${5 * i}`);
}

// 8. Usa un bucle para invertir una cadena de texto

// 9. Usa un bucle para generar los primeros 10 números de la secuencia de Fibonacci

// 10. Dado un array de números, usa un bucle para crear un nuevo array que contenga solo los números mayores a 10