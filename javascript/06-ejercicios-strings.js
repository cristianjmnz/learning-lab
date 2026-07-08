// 1. Concatena dos cadenas de texto
let name = "Cristian"
let saludo = "Hola " + name + "!"

console.log(saludo)
// 2. Muestra la longitud de una cadena de texto
console.log(saludo.length)

// 3. Muestra el primer y último carácter de un string
console.log(saludo[0])
console.log(saludo[14])

// 4. Convierte a mayúsculas y minúsculas un string
console.log(saludo.toUpperCase())
console.log(saludo.toLowerCase())

// 5. Crea una cadena de texto en varias líneas
let texto = `Hola, este
es un texto
en varias lineas`
console.log(texto)

// 6. Interpola el valor de una variable en un string
console.log(`Hola, ${name}!`)

// 7. Reemplaza todos los espacios en blanco de un string por guiones
console.log(saludo.replace(" ", "-"))

// 8. Comprueba si una cadena de texto contiene una palabra concreta
console.log(saludo.includes("christian"))

// 9. Comprueba si dos strings son iguales
let string1 = "Hola"
let string2 = "hola"
console.log(string1 === string2)

// 10. Comprueba si dos strings tienen la misma longitud
console.log(string1.length === string2.length)