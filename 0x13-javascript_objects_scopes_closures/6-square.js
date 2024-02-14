#!/usr/bin/node

const _Square = require('./5-square');

class Square extends _Square {
    charPrint(c){
            if (typeof c === 'undefined') {
              this.print();
            } else {
                for (let i = 0; i < this.height; i++) {
                    str = '';
                    for (let j = 0; j < this.width; j++) {
                        str += c;
                    }
                    console.log(str);
                }
    
            }
    } 
}

module.exports = Square;
