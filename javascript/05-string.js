// Strings (cadena de texto)

// Concatenación

let myName = "Cristian"
let mensage = "Hola, " + myName + "!"
console.log(mensage)
console.log(typeof mensage)

// Longitud

console.log(mensage.length)

// Acceso a caracteres

console.log(mensage[0])
console.log(mensage[6])

// Metodos comunes

console.log(mensage.toUpperCase()) // Mayusculas
console.log(mensage.toLowerCase()) // Minusculas

console.log(mensage.indexOf("Hola")) // Índice
console.log(mensage.indexOf("C"))

console.log(mensage.includes("Hola")) // Incluye
console.log(mensage.includes("Cristian"))
console.log(mensage.includes("Sajiri"))

console.log(mensage.slice(0, 10)) // Sección
console.log(mensage.replace("Cristian", "Jimenez")) // Reemplazo

// Template literals (plantillas literales)

// Strings en varias líneas
let texto = `Hola, este
es mi
curso de
JavaScript`
console.log(texto)

// Interpolación de valores
let email = "cristianjimenez9595@gmail.com"
console.log(`Hola, ${myName}! Tu email es ${email}.`)