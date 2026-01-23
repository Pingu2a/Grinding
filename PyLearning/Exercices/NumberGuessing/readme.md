# Number Guessing

In this game, we need to find a number between 1 and 100. We can also choose the difficulty between 'easy' and 'hard'. If the game is in 'easy' mode, we have 10 lifes, if it's in 'hard' mode, we have 5.

How my logic was :

- Creating a constant who generate a random number between 1 and 100.
- Asking the user the difficulty and saving the data in a variable.
- Asking the user a number to guess until the lifes are down or until he found it 
- At the end of the game, checking if he won or lost, printing a message and asking if the player wants to play again or not

## Logic

<span style="color: blue;">*function number_guessing()*</span>

Main function who manage the whole game. Generating a random number and saving it into a constant during the game. Then asking what difficulty the user wants.
I created a variable 'attempts' who has 10 if the game is in easy mode, 5 if it's in hard mode.
While loop manage the game and asking the user a number ot guess. Loops continue until the attamps are not in 0 and until he won.

At the end of the game, asking the user if he wants to play again or not.