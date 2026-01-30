# The Quizz game !

To start learning OOP, I had to do a quizz game.

Here is how it works :

- We print a question to the user, who has to answer between 'true' or 'false'
- This exercice prints 12 questions so we do it 12 times.
- We save the résult if he found the answer (+1)
- At the end of the game, we print the user's result
- Again, we ask to the user if he wants to play again

<hr>

## How to play

The game starts automaticly. To answer you need to type`true or false`

If you want to leave the game, just type `q`.


<hr>

## Logic

**Function test on main.py**

Main function who manage the game. We print questions and take user's answer. At the end, we print the final result and a little input if he wants to play again or not. User can leave the game at any moment if he writes `'q'`

**Class QuizBrain**


1. `__init_`--> Where the quizz starts. It sets up the question number, the user score and the questions list
2. still_has_question() --> This method checks if the game should continue. It returns *true* if there are still questions to ask, *false* if the quiz is over.
3. `next_question()` --> The main action method ! 
   - It retrieves the current question obj from the list using the *question_number* as an index.
   - It increases the *question_number* by 1 so the next turn will move forward
   - It shows the question text to the user and waits for their input(true/false).
   - Finally, it sends the user's answer to the *check_answer* method to see if they were right.
4. `check_answer()` --> Evaluate player's performance
   - If the user types `q`, it uses *sys.exit()* to close the programm immediately.
   - It compares the user's answer to the correct answer
   - If correct, it pritns a message in green and add +1 to *self.usr_score*.
   - If not, it prints in red.
   - In both cases, the game prints the correct answer
   - After every question, it prints the current score.