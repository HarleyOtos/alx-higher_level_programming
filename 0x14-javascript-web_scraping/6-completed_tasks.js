#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw error;

  const todos = JSON.parse(body);
  const completed = {};

  todos.forEach(function (todo) {
    if (todo.completed) {
      if (completed[todo.userId]) {
        completed[todo.userId]++;
      } else {
        completed[todo.userId] = 1;
      }
    }
  });

  console.log(completed);
});
