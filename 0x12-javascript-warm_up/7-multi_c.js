#!/usr/bin/node

const limit = parseInt(process.argv[2]);

if (limit) {
    for (let i = 0; i < limit.llimit; ++i) {
        console.log('C is fun');
    }
} else {
    console.log('Missing number of occurrences');
}
