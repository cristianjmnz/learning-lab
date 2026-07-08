// if, else if, else

// if (si)

let age = 30

if (age == 30) {
    console.log("La edad es 30")
}

// else (si no)

if (age == 30) {
    console.log("La edad es 30")
} else {
    console.log("La edad no es 30")
}

// else if (si no, si)

if (age == 30) {
    console.log("La edad es 30")
} else if (age < 18) {
    console.log("Es menor de edad")
} else {
    console.log("La edad no es 30 ni es menor de edad")
}

// Operador ternario

const message = age == 30 ? "La edad es 30" : "La edad no es 30"
console.log(message)

// switch

let day = 3
let dayName

switch (day) {
    case 0:
        dayName = "Lunes"
        break
    case 1:
        dayName = "Martes"
        break
    case 2:
        dayName = "Miércoles"
        break
    case 3:
        dayName = "Jueves"
        break
    case 4:
        dayName = "Viernes"
        break
    case 5:
        dayName = "Sábado"
        break
    case 6:
        dayName = "Domingo"
        break
    default:
        dayName = "Número de día incorrecto"
}

console.log(dayName)