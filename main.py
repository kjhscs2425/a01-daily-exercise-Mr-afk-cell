import turtle

def draw_triangle():
    #top line
    turtle.forward (100)

    #triangle line 2
    turtle.right(120)
    turtle.forward(100)

    #triangle line 3
    turtle.right(120)
    turtle.forward(100)

    #reverse line 3
    turtle.right(180)
    turtle.forward(100)

draw_triangle()
draw_triangle()
turtle.right(60*2)
draw_triangle()
draw_triangle()
turtle.right(60*2)
draw_triangle()
draw_triangle()

# turtle.left(120)
# turtle.forward(120)
# turtle.left(120)
# turtle.down(120)
# turtle.forward(120

turtle.exitonclick()