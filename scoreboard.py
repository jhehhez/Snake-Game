from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.highscore = 0
        self.score = 0
        self.write(f"Score: {self.score}", False, 'center', ('Arial', 12, 'normal'))

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", False, 'center', ('Arial', 12, 'normal'))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!! Your score is {self.score}", False, 'center', ('Arial', 12, 'normal'))