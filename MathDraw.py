import turtle

window = turtle.Screen()

slo = turtle.Turtle()
slo.shape('classic')

slo.penup()
slo.setposition(-250, 0)
slo.pendown()

# Racamán sequence

current = 0
seen = set()

for size in range(100):
    backwards = current - size

    if backwards > 0 and backwards not in seen:
        if size % 2:
            slo.color('red')
        else:
            slo.color('green')
        slo.setheading(90)
        slo.circle(5 * size / 2, 180)
        current = backwards
        seen.add(current)

    else:
        slo.setheading(270)
        slo.circle(5 * size / 2, 180)
        current += size
        seen.add(current)

turtle.done()

