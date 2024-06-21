#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const rl = new Rectangle(2, 3);
console.log(rl);
console.log(rl.width);
console.log(rl.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

