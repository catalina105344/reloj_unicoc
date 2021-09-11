k = 0
j = 0
f = 0
def setup ():
    size (250, 250)
def draw():
    background(0)
    global k
    global j
    global f
    circle(25, k, 40)
    if k > height:
       k = 0
    else:
       k = map(second(), 0, 59, 0, height)
    circle(110, j, 40)
    if j > height:
       j = 0
    else:
       j = map(minute(), 0, 59, 0, height)
    circle(200, f, 40)
    if f > height:
       f = 0
    else:
       f = map(hour(), 0, 59, 0, height)
