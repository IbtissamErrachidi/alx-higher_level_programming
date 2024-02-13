#!/usr/bin/node

const argument = process.argv[2];
const converted = parseInt(argument);

if (!isNaN(converted)) {
    for (let i = 0; i < converted; i++) {
	let str = '';
        for (let j = 0; j < converted; j++) {
            str += 'x';
        }
        console.log(str);
    }
} else if (typeof(argument) === 'string')
{
    process.stdout.write('Missing size');
}

