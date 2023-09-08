import turtle
import pandas

from score import Score


FORMAT = ('Arial', 8)
ALIGN = 'center'

class States(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv('50_states.csv')
        self.guessed_correctly = False
        self.check_state = True
        self.hideturtle()
        self.penup()
        self.states_guessed = []
    
    def convert_list_float(self, x_cor, y_cor, user_guessed):
        for i in x_cor:
            x_cor = float(i)

        for i in y_cor:
            y_cor = float(i)
        
        self.state_printing(x_cor, y_cor, user_guessed)

    def user_input(self):
        user_guessed = turtle.textinput('Enter name', 'Enter US State name')
        user_guessed = user_guessed.title()
        self.guessing(user_guessed)
    
    def state_printing(self, x_cor, y_cor, user_guessed):
        self.goto(x=x_cor, y=y_cor)
        self.write(user_guessed, align=ALIGN, font=FORMAT)

    def guessing(self, user_guessed):
        self.guessed_correctly = False
        for states in self.states_guessed:
            if user_guessed == states:
                print("Already Guessed")
                self.check_state = False
                break
            else:
                self.check_state = True

        if user_guessed in self.data.state.values and self.check_state:
            self.states_guessed.append(user_guessed)
            state = self.data[self.data.state == user_guessed]
            x_cor = state.x.to_list()
            y_cor = state.y.to_list()
            self.guessed_correctly = True
            self.convert_list_float(x_cor=x_cor, y_cor=y_cor, user_guessed=user_guessed)


