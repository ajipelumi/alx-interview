## Star Wars Api

## Description
This is a script that prints all characters of a Star Wars movie.

### Example:
```node
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

### Files:
[0-starwars_characters.js](0-starwars_characters.js)

### Explanation:
The script receives a number as argument, this number is the episode number of a Star Wars movie.
Then, it makes a request to the Star Wars API to get the characters of that movie and prints them in order.

We import the request module first, then we get the episode number using `process.argv[2]`.
After that, we make the request to the API using the `request` module and the `episode number` as argument.

The request returns a JSON object with the characters of the movie, we iterate over the characters and print them.