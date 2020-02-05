#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  exports.nb = 1;
  theFunction(exports.nb + number);
  exports.nb++;
};
