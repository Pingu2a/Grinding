# Pong Game

For this project, I created the classic Pong game using Python and the Turtle library!

I developed the project step by step:
1. Create and setup the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with walls and bounce
6. Detect collision with paddles
7. Detect when paddle misses
8. Keep score

## Logic

The logic explained for each file.

**File [main]**

This file acts as the central coordinator. It manages the game loop and handles the high-level logic of physics and collisions between different objects.

1.Setup and Configuration
 - **Screen Management**: Initializes an 800x600 pixel window.
 - Animation Control (`tracer(0)`): Disables the default animation to allow for custom frame updates. This is crucial for Pong to ensure that paddles and the ball move in sync without flickering.
- **Object Instantiation**: Creates the two paddles (left and right), the ball, and the scoreboard.

2.User Input & Controls
  - **Event Listening**: Uses `screen.listen()` to capture inputs.
  - **Fluid Movement Logic**: Instead of simple "onkey" events that jump, it uses a combination of `onkey` and `onkeyrelease` to update a direction variable. This allows players to hold a key for smooth, continuous movement.

3.The Core Game Loop

-  **Movement**: Calls the `.move()` method for both paddles and the ball at every cycle.
- **Wall Collision**: Detects if the ball hits the top or bottom (y-axis) and triggers the `.bounce_y()` method.
- **Paddle Collision**: Uses the `.distance()` method combined with x-coordinates to check if the ball hits a paddle. If triggered, the ball bounces and increases speed.
- **Score Tracking**: Detects if the ball goes past the left or right boundaries. It then resets the ball position and updates the respective player's score.

**File [Paddle]**

This class handles the creation and behavior of the paddles.
- **Inheritance**: Inherits from `Turtle`.
- **Initialization**: Sets the shape to a "square" and uses `shapesize(stretch_wid=5, stretch_len=1)` to turn the square into a vertical rectangle.
- **Directional Logic**:
    - `go_up()` / `go_down()`: These methods don't move the paddle directly; they set a `self.direction` variable.
    - `stop()`: Sets the direction back to 0 when the key is released.
- `move()` **Method**: Calculates the new position based on the current direction. It includes a constraint to prevent the paddle from moving off-screen.

**File [Ball]**

The `Ball` class manages the physics of the game's projectile.

- **Movement Logic**: Uses `x_move` and `y_move` attributes. Every time `move()` is called, the ball's coordinates are incremented by these values.
- **Bouncing**:
    - `bounce_y()`: Multiplies `y_move` by -1 (reverses vertical direction).
    - `bounce_x()`: Multiplies `x_move` by -1 (reverses horizontal direction) and multiplies `move_speed` by 0.9 to make the game faster and harder.
- **Reset**: When a player scores, `reset_position()` sends the ball back to (0,0) and resets the speed to the original value.

**File [Scoreboard]**

The `Scoreboard` class manages the UI and the win/loss state.
- **Attributes**: Tracks l_score and r_score independently.
- **Display**: Uses the `.write()` method twice at specific coordinates to show the scores for both sides of the field.
- `update_scoreboard()`: Clears the previous score and redraws the current state. This is called every time a player misses the ball.

<hr>

By separating the project into 4 files, the code is modular and easy to maintain:
- To change the game's difficulty, I can simply adjust the `move_speed` in `ball.py`.
- To change the paddle size or speed, I only edit `paddle.py`.
- To modify the scoring rules or screen size, I edit `main.py`.