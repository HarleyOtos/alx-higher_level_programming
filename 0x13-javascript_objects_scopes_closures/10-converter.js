#!/usr/bin/node

exports.converter = function (base) {
  function theCoverter (n) {
    return n.toString(base);
  }

  return theCoverter;
};
