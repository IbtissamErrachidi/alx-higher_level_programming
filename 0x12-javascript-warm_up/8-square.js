#!/usr/bin/node

const argument = process.argv[2];
const converted = parseInt(argument);

if (!isNaN(converted)) {
    for (let i = 0; i < converted; i++) {
        for (let j = 0; j < converted; j++) {
            process.stdout.write('x');
        }
        console.log(); 
    }
} else if (typeof(argument) === 'string') { 
    console.log('Missing size');
} else {
    return;
}

