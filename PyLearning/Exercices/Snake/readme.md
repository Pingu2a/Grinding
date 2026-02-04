# Snake Game

For this project, I had to create the famous Snake Game!

I created the project step by step :

1. Create a snake body
2. Moving the snake
3. Controlling the snake
4. Detect collision with food
5. Create a scoreboard
6. Detect collision with wall --> Game Over
7. Detect collision with tail --> Game Over


## Logic


The logic explained for each files.

**File [main]**

This file acts as the game engine and coordinator. It uses Object-Oriented Programming (OOP) to manage the interactions between the snake, its food, and the scoring system.

1. Setup and Configuration
   - Screen Management (`Screen`): Initializes a 600x600 pixel window with a black background.

    - Animation Control (`tracer(0)`): Disables automatic animations. This allows the program to calculate movements in the background and only refresh the display when the calculation is complete via `screen.update()`. This ensures smooth, lag-free movement.

    - Object Instantiation: Creates the three core objects: snake, food, and scoreboard.
<br>
1. User Input & Controls
    - Event Listening (`screen.listen`): Sets the screen to capture keyboard inputs.
    - Key Mapping: Links the arrow keys to the corresponding direction methods in the Snake class (`up`, `down`, `left`, `right`).
<br>

3. The Core Game Loop (`while game_on`)
The game logic runs inside a continuous loop, updating every 0.1 seconds to check for three critical conditions:

   - Movement: The snake moves forward one step during every cycle.

   - Food Collision: Uses the `.distance()` method to check if the
  snake's head is within 15 pixels of the food. If true:

    - The food teleports to a new random location (`refresh`).
    - The snake grows by one segment (`extend`).
    - The score is updated on the display (`increase_score`).

   - Collision Detection (Game Over):

     - Wall Collision: Checks if the head's `xcor` or `ycor` coordinates exceed the +/- 280 pixel boundaries.

      - Tail Collision: A for loop iterates through all segments (skipping the head). If the head's distance to any segment is less than 10 pixels, a collision is triggered.
<br>

4. Game Exit
When a collision is detected, `game_on` is set to **False**. The `scoreboard` displays a "GAME OVER" message, and the program waits for a user click to close the window and return to the main arcade menu.

**File [Snake]**

This class manages the appearance, movement, and growth of the snake. It handles the complex logic of making multiple independent segments move as a single, cohesive unit.

1. Constants and Configuration
To make the code easy to maintain, several constants are defined at the top:
   - `START_POS`: A list of tuples defining the initial coordinates of the first three segments.
   - `MOVE_DISTANCE`: Set to 20 pixels, matching the size of the turtle squares to ensure perfect grid movement.
    - **Directions**: Standardized angles (UP=90, DOWN=270, etc.) to prevent "magic numbers" in the code.
<br>

1. Segment Management
    - `__init__`: When a `Snake` object is created, it initializes an empty list of segments and automatically triggers the creation of the starting body. It also identifies self.head as the first segment for easier access.
    - `add_segment(position)`: This helper method handles the creation of individual body parts, ensuring they are all green squares with their pens up to avoid drawing lines.
    - `extend()`: This method is called whenever the snake eats food. It adds a new segment at the exact position of the current last segment (`self.segments[-1]`), causing the snake to grow.
<br>

3. The "Follow the Leader" Movement
The `move()` method contains the most critical logic:

    - **The Problem**: If you move all segments forward, they would overlap or move in parallel.
    - **The Solution**: The segments move in reverse order. A `for` loop iterates from the last segment up to the first one.
    - **The Logic**: Each segment moves to the coordinates of the segment that was previously in front of it.
       - Segment 3 moves to Segment 2's old position.
      - Segment 2 moves to Segment 1's old position.
      - Finally, the **Head** (Segment 0) moves forward.
   - This creates the classic "slithering" effect where the body follows the path of the head perfectly.
<br>

1. Directional Constraints
The methods `up()`, `down()`, `left()`, and `right()` control the head's heading. However, they include logic to prevent illegal moves:

    - In the game of Snake, the player cannot perform an immediate 180-degree turn (e.g., you cannot go directly from UP to DOWN).

    - The Logic: Before changing the heading, the code checks the current direction. For example, `up()` will only execute if the current heading is not `DOWN`.
<br>

**File [food]**

The `Food` class is responsible for generating the target objects the snake must "eat."

-   **Inheritance**: This class inherits from the Turtle class. This is a powerful OOP concept because the Food object is a Turtle, meaning it immediately gains all the methods for movement, shape, and color.

-   **Initialization**:

    - The shape is set to a "circle" (or your custom "poisson.gif").
    - The size is reduced using `shapesize(0.5, 0.5)` to make it half the standard size.
    - `penup()` is called to ensure no lines are drawn when it moves.

- `refresh()` **Method**: Instead of creating a new object every time, the same object is simply teleported to a new random location on the screen using `random.randint(-280, 280)`. This is much more efficient for memory than constant creation and deletion.

<br>

**File [scoreboard]**

The `Scoreboard` class manages the UI (User Interface) and tracks player progress.

- **Inheritance**: Like the food, it inherits from `Turtle`. However, the turtle itself is hidden (`hideturtle()`) because we only want to see the text it writes.

- **Attributes**: It maintains an internal score variable initialized at 0.

- `update_scoreboard()`: This is a central method that clears the previous text and writes the current score. It uses the `.write()` method with specific parameters for alignment (*center*) and font style.

- `increase_score()`:
1.Increments the score variable.
2.Clears the old text (using `self.clear()`).
3.Calls `update_scoreboard()` to display the new value.

- `game_over()`: Triggered when a collision occurs. It teleports the invisible turtle to the center of the screen (0,0) and writes "GAME OVER" in a large font.

<hr>

By separating the project into 4 files, It's easier to read and to modify :

- If I want to change snake's speed, I only edit `snake.py`
- If I want to change the font of the score, I only edit `scoreboard.py`
- If I want to add a new game mode, I only edit `main.py`