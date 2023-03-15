#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');
let content = '';

content = content.concat(fs.readFileSync(process,argv[2]));
content = content.concat(fs.readFileSync(process,argv[3]));
fs.writeFileSync(process.argv[4], content);
