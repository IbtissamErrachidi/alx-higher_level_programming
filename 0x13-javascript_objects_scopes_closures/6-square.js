#!/usr/bin/node

const _Square = require('./5-square');

class Square extends Rectangle {
    constructor(size){
        super(size,size);
    }
    charPrint(c){
        if(typeof c !== 'undefined'){
            for (let i = 0; i < this.height; i++) {
                for (let j = 0; j < this.width; j++) {
                    process.stdout.write(c);
                }
                console.log();
            }
        }
        else{
            this.print();
        }
    }
    
}

module.exports = Square;
