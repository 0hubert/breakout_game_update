from turtle import Turtle
ALIGNMENT = "center"
FONT=("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over - Press Space to Restart", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()

    def game_won(self):
        self.clear()
        self.goto(0, 0)
        self.write("YOU WIN! Press SPACE to play again", align="center", font=("Arial", 24, "normal"))