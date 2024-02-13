#!/usr/bin/node
const first = process.argv[2];
const convert1 = parseInt(first);
const second = process.argv[3];
const convert2 = parseInt(second);
function add(a, b){
    if(!isNaN(a) && !isNaN(b)){
        return a+b;
     }
}

console.log(add(convert1,convert2));
