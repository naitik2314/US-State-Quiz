from turtle import Screen
from score import Score
from states import States
import time

#Initializing the screen
screen = Screen()
screen.bgpic('blank_states_img.gif')

#Timer
duration = 10 * 60
start_time = time.time()

#Turning the game loop/initializing the game loop
game_is_on = True

#Initialize Score
score = Score()

#Intialize States
states = States()

#Game Loop
while game_is_on:
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(elapsed_time)
    if elapsed_time >= duration:
        score.time_over()
        game_is_on = False

    states.user_input()
    if states.guessed_correctly:
        score.score += 1
        score.update_scoreboard()
    if score.score == 50:
        score.won()
        game_is_on = False

#Screen exit condition
screen.exitonclick()