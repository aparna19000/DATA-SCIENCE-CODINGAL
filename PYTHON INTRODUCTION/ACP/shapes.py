import turtle

screen = turtle.Screen()
screen.setup(width=900, height=500)
screen.title("Drawing Polygons with Turtle")
screen.bgcolor("#2C3E50")  

artist = turtle.Turtle()
artist.shape("turtle")
artist.speed(3)  
artist.pensize(3) 


def move_to(x, y):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()


# ---  Draw Equilateral Triangle ---
# Internal angles are 60°, so turtle must turn 180° - 60° = 120°
move_to(-250, -50)
artist.color("white", "#E74C3C") 

artist.begin_fill()
for _ in range(3):
    artist.forward(120)
    artist.left(120)
artist.end_fill()

# --- Draw Rectangle ---
# Opposite sides are equal, all internal angles are 90°
move_to(-50, -50)
artist.color("white", "#3498DB")  

artist.begin_fill()
for _ in range(2):
    artist.forward(160)  # Length
    artist.left(90)
    artist.forward(100)  # Width
    artist.left(90)
artist.end_fill()

# ---  Draw Hexagon ---
#  sides. External turn angle is 360° / 6 = 60°
move_to(180, -50)
artist.color("white", "#2ECC71")  

artist.begin_fill()
for _ in range(6):
    artist.forward(80)
    artist.left(60)
artist.end_fill()

# ---  Wrap Up ---
# Hide the turtle icon when done and keep the window open
artist.hideturtle()
screen.mainloop()