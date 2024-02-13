#!/usr/bin/node
const first = parseInt(process.argv[2]);
function fact(a){
    fac = 1;
    for(i=1;i<=first;i++)
        fac*=i;
    return fac;
}

console.log(fact(first));
