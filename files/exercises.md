# Files exercises

## Exercise 1: User data in "Guess number game" (GNG)

Add new functionality to your GNG, to persist some data about player.

1. Each new game iteration game asks user to input a _username_.
2. If user played game earlier game outputs: ```"Hey, {username}, nice to see you! You played game: {amout_games} times"``` amout of games should track how many times user played GNG.
3. If given _username_ is a new one, so program outputs: ```"Hey, {username}, welcome! Lets play your first game".```
4. Remember that user can quit the game in the middle of a round, be sure not to fail in that case, count statistics only after round is completed.
5. **Optional Task:** add track of how many guesses user made during all game sessions, to calculate statistics of average guess_score = total_guesses / amout_games.


## Ex 2: 

Write a script that will parse example.json, and extract name, email, age for each user and save it into new .csv file in the following format:

```csv
name,age,email
Donald Cook,50,donald@gmail.com
Gevin Belson,49,gavin.b@hooli.com
...
```

## Ex 3 (csv):

:TODO
