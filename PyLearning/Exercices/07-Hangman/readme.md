Hangman Game ! This famous game was not that easy to do tbh.

First, I didn't really know how to begin. I wrote on a papaer what I need to do.

How I did :

1. Creating a list with the graphic Hangman, and a list with 20 differents words (animals here)
2. Create `blank`variable to print "-" representing the hidden word
3. Checking if user put a good letter
4. If not, I need to remove a life
5. The game is finish once the user found the word or the user's lifes are finished


# Logic

**Colors** 

*lines 6-10*

The colors are just for the print's. Added green if user wins, red if he losts and yellow for the replay

**Clearing the terminal**

*lines 13-14*

Added this little function to clear the terminal during the game to make this clean. I clean the terminal once the game is finished too.

**Lists**

*lines 18-84*

First list is the hangmang stage. I can use it if he lost life juste need to change the index. The second list stands for the animals name to find. In this hangman, you need to find animals names.

**Game()**

*lines 88-138*

This function is the main function of my game. I did this function to choose after if I want to play again or not

**Main variables**

*lines 93-96*

I created these main variables :

- `secret word` = choosing a random word in the list animals
- `blank`= This variable will show "-" for the hidden word
- `life`= User's lifes
- `wrong_letters` = An empty list who will store all the wrong letters the user typed


**While True 1st part**

*lines 100-125*

In this loop, We have :
- the input user to choose a letter, checking if he puts 1 or more letters or if he puts a letter twice.
- A condition to check if the word the user typed is in the secret word (if yes, changing the `blink`and replace by the letter in the good position. If not, removing 1 life and adding the wrong letter into the list `wrong_letters`)
- the prints for the user (hangman stage, wrong letters, blank and user's life(s))

**While True 2nd part**

*lines 129-138*

In the last part of this loop, we can find how the game will be finish. The first if checks if the user found the secret word, the second if is for the loosing situation.


**While true for replay**

*lines 142-149*

With this loop, I can do a replay. If the user want to play again, the game starts again. If the user want to leave, I just print goodbye or smth else.