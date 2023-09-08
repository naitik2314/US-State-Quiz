from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open ('high_score.txt', mode='r') as file:
            contents = file.read()
            contents = int(contents)
        self.high_score = contents
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=200, y=360)

    def game_start(self):
        self.write(f'{self.score}/50, Highscore = {self.high_score}', align='center', font=('Arial', 15))
    
    def update_scoreboard(self):
        self.clear()

        self.write(f'{self.score}/50, Highscore = {self.high_score}', align='center', font=('Arial', 15))

    def won(self):
        self.clear()
        self.goto(0, 0)
        self.write('You won!')
        if self.score > self.high_score:
            self.high_score = self.score
            with open ('high_score.txt', mode='r+') as file:
                file.write(self.high_score)
            
    def time_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Time over!, your score = {self.score}", align='center', font=('Arial', 15))
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score = str(self.high_score)
            with open ('high_score.txt', mode='r+') as file:
                file.write(self.high_score)