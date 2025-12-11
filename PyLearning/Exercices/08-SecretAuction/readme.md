<h1 align="center" style="color:green">Secret auction</h1>

### Exercice goal
<br>
The goal of this exercise is to create a simple secret auction program in Python where each user can enter their name and bid. At the end, the programm determines the highest bidder an displays the winner.
<br><br>

### Logic
<br>
I used a simple logic to make this exercice :

- Asking the user name and the price
- Saving the datas in a dictionary
- Asking if other bidders wanted to play
- If yes, Im asking again name, price, and saving these datas in the dicitonary
- If no, I create a function to find the highest bidder and return it
<br><br>

### Build the thing 
<br>
This exercice was simple so here is how I coded :

1. Create an empty dictionary called `bid`
2. Create a while loop because at the end, I'm asking is other users want to play
3. Asking for users infos then I'm saving these datas in `bid``
4. If nobody else want to bid, it's time to find who is the highest bidder !
5. Create a function who take in param the dictionary `bid`
6. Inside this function, only this code works to find the highest one :
```python
    for name, bid in bids.items():
        if bid > highest_bid:
            winner = name
            highest_bid = bid
```
7. In the function, return a print with the winner
8. At the end when I do this function, I added a small function to print all the bidders and their prices to see who was there
9. A little `break`to 


> I know break is not really good to end the program cuz he only cuts the loop but for little programs it works fine lol

<br>

### What I learned

With this exercice I learned some cool things :
- Dictionaries in python, How to use them, manipulate them
- Looping trough dictionary items
- How to store datas in a dictionary
- How to compare values and determine a max


*I also learned few cool things about readme so now I can properly build good readme heheh*

![pingu](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3R0bHNia2xoaGRlMHQ3bGQ5bGlhemF4NGZjNnczbTNnbGNxMXVtYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iDPv54rvXkkA8/giphy.gif)