#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    const data = response.body;
    const characters = JSON.parse(data).characters;
    characters.forEach(character => {
      request(character, (error, response) => {
        if (error) {
          console.error(error);
        } else {
          const data = response.body;
          const name = JSON.parse(data).name;
          console.log(name);
        }
      });
    });
  }
});
