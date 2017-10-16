from turtle import*



def facade () :
    for loop in range (4):
        fd(100)
        lt(90)

def toit () :
    penup()
    left(90)
    goto(100,100)
    pendown()
    lt(30)
    for loop in range (3):
        fd(100)
        lt(120)
        
def porte () :
    penup ()
    goto (50,0)
    pendown ()
    rt (30)
    fd (50)
    rt (90)
    fd (25)
    rt (90)
    fd (50)

def fenetre () :
    penup ()
    goto (7,60)
    pendown ()
    position()
    heading()
    circle(15)
def fenetre2 () :
    penup ()
    goto (30,120)
    pendown()
    position()
    heading()
    circle (15)

def arbre () :
    penup ()
    goto (100,200)
    pendown
    position()
    
