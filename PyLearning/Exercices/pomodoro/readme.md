# Pomodoro Timer 
The Pomodoro technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This application automates that cycle with a clean, visual interface.

This project focuses on **advanced Tkinter concepts**, specifically the Canvas widget for layering elements and the `.after()` method for creating a non-blocking countdown mechanism.


## How to try
Navigate to /PyLearning/Exercices and run the `main.py` file.

The app will automatically cycle through:
- Work (25 min)
- Short Break (5 min)
- Long Break (20 min) every 4 work sessions.

Click "**Reset**" at any time to stop the timer and return to zero.

## Logic

1. **The Canvas Widget**

    Unlike a standard Label, the `Canvas` allows us to layer a `PhotoImage` (the tomato) and text (the timer) at specific pixel coordinates. This creates the professional look of text sitting "inside" the image.
    <br>
    *Note*: We used `highlightthickness=0` to remove the default border and `canvas.image = tomato_img` to prevent Python's Garbage Collector from deleting the image from memory.
<br>
2. **The Countdown Mechanism**(`window.after`)
In a GUI, you cannot use a standard `while loop` or `time.sleep()`, as they would freeze the window. Instead, we use `window.after(1000, function)`. This tells Tkinter to wait 1 second and then execute the function again, allowing the interface to stay responsive while the clock ticks.
<br>
3. **Dynamic Typing for Formatting**
To keep the "00:00" format, we used Python's **Dynamic Typing**. If the seconds drop below 10, the variable `count_sec` is converted from an `int` to a `f-string` (e.g., 5 becomes "05") so it displays correctly on the screen.
<br>
4. **Session Tracking**
A global variable reps tracks how many sessions have passed:
    - **Odd Reps**: Work session.
    - **Even Reps**: Short break.
    - **Rep 8, 16, etc.**: Long break.
        After every two reps (one work session), a checkmark `✓` is added to the bottom of the screen to track progress.