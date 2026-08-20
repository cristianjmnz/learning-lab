// Funciones

// Simple

function myFunc() {
    console.log("¡Hola, función!")
}

for (let i = 0; i < 2; i++) {
    myFunc()
}

// Con parámetros

let name = "Cristian";
function myFuncWithParams(name) {
    console.log(`¡Hola, ${name}!`)
}

myFuncWithParams(name);