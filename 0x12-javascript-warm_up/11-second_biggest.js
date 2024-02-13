#!/usr/bin/node
const args = process.argv;
const argsLength = args.length;
if(argsLength <= 3)
{
    console.log(0);
}
else{
    max = args[2];
    for(let i=3;i<argsLength;i++){
        if(max<args[i]){
            max = args[i]
        }
    }
    console.log(max);
}
