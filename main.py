import turtle
import pandas
from state_names import States_US

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_states = pandas.read_csv("50_states.csv")

us_states_list = us_states["state"].to_list()

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = [state for state in us_states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in us_states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = us_states[us_states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

#states_to_learn.csv
screen.exitonclick()
