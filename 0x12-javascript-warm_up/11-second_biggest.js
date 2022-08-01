#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const seclast = process.argv.sort((a, b) => b - a);
  console.log(seclast[3]);
}
