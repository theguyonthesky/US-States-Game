import turtle
import os

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv('50_states.csv')
states_list = data.state.to_list()
guessed_states = []

if os.path.exists('states_to_learn.csv'):
    os.remove('states_to_learn.csv')

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt="What's the another state's name?").title()


    if answer_state == 'Exit':
        missed_states = [state for state in states_list if state not in guessed_states]
        # missed_states = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        print(missed_states)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        #move to a particular location in map ; to do this we need to create a turtle
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_coordinate = data[data.state == answer_state]
        t.goto(state_coordinate.x.item(), state_coordinate.y.item()) #to get x and y coordinates we need to tap into the csv again and get each row item
        t.write(answer_state, align='center', font=('Arial', 12, 'normal'))

