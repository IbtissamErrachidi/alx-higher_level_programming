#!/usr/bin/node



const argument = process.argv[2];
const converted = parseInt(argument);

if (!isNaN(converted)) {
    for (let i = 0; i < converted; i++) {
        let str = '';
        for (let j = 0; j < converted; j++) {
            str += 'X';
        }
        console.log(str);
    }
} else {
    console.log('Missing size');
}

