import turtle
import pandas


def play_states_game():
    screen = turtle.Screen()
    screen.title("US States Game")
    screen.setup(width=725, height=491)
    image = "Exercices/States/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("Exercices/States/50_states.csv")
    states = data["state"].to_list()
    score = 0
    guessed = []

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()

    while score < 50:
        answer_state =screen.textinput(title=f"{score}/50", prompt="What's another state name ? ").title()

        if answer_state == "Exit":
            missing_states = [state for state in states if state not in guessed]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("Exercices/States/states_to_learn.csv")
            break
        if answer_state in states and answer_state not in guessed:
            score += 1
            guessed.append(answer_state)
            state_data = data[data.state == answer_state]
            writer.goto(int(state_data.x.item()), int(state_data.y.item()))
            writer.write(answer_state, align="center", font=("Arial", 8, "normal"))