#!/usr/bin/node
exports.nbOccurences = (list, searchElement) =>
list.filter((e) => (e === searchElement)).length;
