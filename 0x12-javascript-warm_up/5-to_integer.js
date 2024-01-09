#!/usr/bin/env node

const num = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
