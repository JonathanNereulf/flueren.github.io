from turtle import *
J = turtle.Pen()

while True:
    J.forward(200)
    J.left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
