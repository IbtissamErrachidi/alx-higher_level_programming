#!/usr/bin/node
const arg = process.argv[2]; 

if (!isNaN(arg)) {
    console.log(`My number: ${Math.floor(Number(arg))}`);
} else {
    console.log("Not a number");
}

