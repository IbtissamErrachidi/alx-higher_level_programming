#!/usr/bin/node
const argument = process.argv[2];
const converted = parseInt(argument);

if (!isNaN(converted)) {
    for (let i = 0; i < converted; i++) {
        for (let j = 0; j < converted; j++) {
            console.log('x'); // Utilisez process.stdout.write pour imprimer sans ajouter de nouvelle ligne
        }
        console.log(); // Nouvelle ligne après chaque ligne d'x
    }
} else { // Utilisez '===' pour comparer le type de variable
    console.log('Missing size');
}
