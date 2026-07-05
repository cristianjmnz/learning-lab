// Tipos de datos primitivos

// String
let name = "Cristian"
let alias = "Sajiri"
console.log(name, alias)

// Number
let age = 30 // Entero
let altura = 1.70 // Decimal
console.log(`Tengo ${age} años y`, `mido ${altura} m`)

// Boolean
let isTeacher = false
let isStudent = true
console.log(`Soy profesor: ${isTeacher}.`)
console.log(`Soy estudiante: ${isStudent}`)

// Undefined
let undefinedValue
console.log(undefinedValue)

// Null
let nullValue = null

// Symbol

let mySymbol = Symbol("mysymbol")

// BigInt

let myBigInt = BigInt(817239871289371986589716389471628379612983761289376129)
let myBigInt2 = 817239871289371986589716389471628379612983761289376129n

// Mostramos los tipos de datos
console.log(typeof name)
console.log(typeof age)
console.log(typeof isTeacher)
console.log(typeof undefinedValue)
console.log(typeof nullValue)
console.log(typeof mySymbol)
console.log(typeof myBigInt)
