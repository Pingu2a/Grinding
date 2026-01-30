# Hirst painting project

This little project was used to learn the turtle python module (https://docs.python.org/3/library/turtle.html#)

This program creates a painting like [Hirst](https://www.myartbroker.com/artist-damien-hirst/collection-spots) painting.

Here is how it works :

- Importing `Turtle` module, initializing our window, turtle and pen
- We use [colorgram](https://pypi.org/project/colorgram.py/) module to extract the colors from an image.
- We put each color in an array
- We draw the painting

<hr>

## How to play

Nothing to do. It runs automaticly. To close the window, just click on it.

## Logic :

*lines 9 - 17*

We initialize the turtle, the pen color and size and the speed

*line 20*

This line extracts colors from *hirst.jpg*

*lines 22 - 28*

We add the colors in an array. The colors are tuple (r,g,b)

*lines 30 - 34*

Setting up where we want to start to draw.

*lines 36 - 45*

We draw the painting in 10x10 grid.

*line 48-49*

With thes lines, we can close the window by clicking on it.