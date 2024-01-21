from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\sumuk\PycharmProjects\snake_game\hs.txt") as hss:
            self.high_score = int(hss.read())
        self.penup()
        self.color("white")
        self.goto(x=0,y=250)
        self.hideturtle()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def gain_score(self):
        self.score += 1
        self.clear()
        self.write(f'\nScore: {self.score}----High Score: {self.high_score}', align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        if(self.score>self.high_score):
            self.high_score = self.score
            with open("../../OneDrive/Desktop/hs.txt", mode="w") as hs:
                hs.write(str(self.high_score))


        self.goto(x=0, y= 0)
        self.write(f'Score: {self.score}\nGame over\nHigh Score: {self.high_score}', align=ALIGNMENT, font=FONT)

