# Blackjack game

Blackjack game was one of the most interseting and difficult projet lol.

Here is how to play :

https://en.wikipedia.org/wiki/Blackjack

Here is how my logic was to do this projet :

- Creating a dictionary with the cards values
- Creating a list with cards icons ("♣", "♠", "♥", "♦")
- Asking the user how much money he want to bet (He start with 100$)
- Creating a function who gives random card (function for the user and the computer)
- Then I give the 2 random cards for the begining of the game to the user and the computer
- User must see his cards and only 1 card of the computer
- After that, I wanted to chek directly if the user has a BlackJack or not
- If not, I created a bloc of code to ask the user to pull a card or no 
- I the user stopped pulling cards, The copmuter need to pull cards until he gets 17 or higher.
- At then end, I just have to check who wins the game and if the user want to play again 


## Logic

<span style="color: blue;">*function play_one_game*</span>

Main function who manage the whole game. First, The function manage if the user bet enough money or not higher than is money in the ban. Then I give randomly 2 cards to the user and the computer. I need to calculate to value of the card so I created a function called <b><span style="color: green;">hand_value</span></b>. 

I check directly if the user gets Blackjack. If not, I ask to the user if he wants to pull a card or not. One he pulled card(s), I break and manage the computer cards.

For the computer cards, I check directly again if the computer has a Blackjack. If not, I Make the computer pull card until he's cards values reach 17 or higher.

Next, I compare user and computer values to see who won with the function <b><span style="color: green;">winner</span></b>. 

At the end of the program, I manage if the player wants to player again or not and if he has enough money to play again or not.


<span style="color: blue;">*function draw_card*</span>

This function return randomly a card with the value and the sign.

<span style="color: blue;">*function hand_value*</span>

This function calculate the value of the hand (user and computer) and manage Ace because ace's value change between 1 or 11.

<span style="color: blue;">*function winner*</span>

This function checks who's the winner.

<span style="color: blue;">*function Blackjack*</span>

This function launch the game and choosing to play again or not.