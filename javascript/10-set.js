// Set

// Declaración

let mySet = new Set()

console.log(mySet)

// Inicialización

mySet = new Set(["Cristian", "Jimenez", "sajicri", 30, true])

console.log(mySet)

// Métodos comunes

// add y delete

mySet.add("https://github/cristianjmnz")

console.log(mySet)

mySet.delete("https://github/cristianjmnz")

console.log(mySet)

console.log(mySet.delete("Jimenez"))
console.log(mySet.delete(4))

console.log(mySet)

// has

console.log(mySet.has("Cristian"))
console.log(mySet.has("Jimenez"))

// size

console.log(mySet.size)

// Convertir un set a array
let myArray = Array.from(mySet)
console.log(myArray)

// Convertir un array a set

mySet = new Set(myArray)
console.log(mySet)

// No admite duplicados

mySet.add("cristianjimenez9595@gmail.com")
mySet.add("cristianjimenez9595@gmail.com")
mySet.add("cristianjimenez9595@gmail.com")
mySet.add("cristianjimenez9595@gmail.com")
console.log(mySet)