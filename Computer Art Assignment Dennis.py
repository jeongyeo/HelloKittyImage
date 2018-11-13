###############################################################################
# Title: Graphics Image.
# Programmer: Dennis Park
# Last modified: 12/10/2014
# Purpose: This program draws a graphical picture.
###############################################################################

# Import Packages
from tkinter import*
from time import*
from random import*
from math import*

# Canvas
myInterface = Tk()
screen = Canvas(myInterface, width=1000, height=750, background="white")
screen.pack()
screen.create_rectangle(0, 0, 1000, 1000, fill="#FFC0FF")


# Gradint Background
def getHexadecimalValue(n):
    digits = "%X" % n
    if len(digits)==1:
          digits = "0" + digits

    return digits


for shade in range(0,256):
    rColor = getHexadecimalValue( 255-shade )
    color = "#FFC0" + rColor

    x = 3 * shade + 200

    screen.create_rectangle( 0, x, 1000, x+3, fill = color, outline = color)


# Random snow-hearts, large to small sized hearts
# Defalt Colour
colour = "snow"

# Parameters
x = -120
y = 0
xx = 0
yy = 0
numHeart = 8
for lHeart in range(1, numHeart + 1):
    x = x + 120
    y = y + 120
    xx = 150
    yy = 200
    xHeart = randint(x, y)
    yHeart = randint(xx, yy)
    c = randint(1,2)
    if c == 1:
        colour = "MistyRose"
    else:
        colour = "snow"
    screen.create_oval(xHeart+10, yHeart+10, xHeart+30, yHeart+30, fill=colour, outline=colour)
    screen.create_oval(xHeart+25, yHeart+10, xHeart+45, yHeart+30, fill=colour, outline=colour)
    screen.create_polygon(xHeart+10, yHeart+23, xHeart+45, yHeart+23, xHeart+27.5, yHeart+50, fill=colour, outline=colour)

x = -100
y = 0
xx = 0
yy = 0
numHeart = 9
for mHeart in range(1, numHeart + 1):
    x = x + 100
    y = y + 100
    xx = 60
    yy = 160
    xHeart = randint(x, y)
    yHeart = randint(xx, yy)
    c = randint(1,2)
    if c == 1:
        colour = "MistyRose"
    else:
        colour = "snow"
    screen.create_oval(xHeart+10/2, yHeart+10/2, xHeart+30/2, yHeart+30/2, fill=colour, outline=colour)
    screen.create_oval(xHeart+25/2, yHeart+10/2, xHeart+45/2, yHeart+30/2, fill=colour, outline=colour)
    screen.create_polygon(xHeart+10/2, yHeart+23/2, xHeart+45/2, yHeart+23/2, xHeart+27.5/2, yHeart+50/2, fill=colour, outline=colour)

x = -40
y = 0
xx = 0
yy = 0
numHeart = 24
for sHeart in range(1, numHeart + 1):
    x = x + 40
    y = y + 40
    xx = 10
    yy = 70
    xHeart = randint(x, y)
    yHeart = randint(xx, yy)
    screen.create_oval(xHeart+10/5, yHeart+10/5, xHeart+30/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_oval(xHeart+25/5, yHeart+10/5, xHeart+45/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_polygon(xHeart+10/5, yHeart+23/5, xHeart+45/5, yHeart+23/5, xHeart+27.5/5, yHeart+50/5, fill=colour, outline=colour)

x = -75
y = 0
xx = 0
yy = 0
numHeart = 15
for sHeart in range(1, numHeart + 1):
    xx = 130
    yy = 150
    x = x + 75
    y = y + 75
    xHeart = randint(x, y)
    yHeart = randint(xx, yy)
    screen.create_oval(xHeart+10/5, yHeart+10/5, xHeart+30/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_oval(xHeart+25/5, yHeart+10/5, xHeart+45/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_polygon(xHeart+10/5, yHeart+23/5, xHeart+45/5, yHeart+23/5, xHeart+27.5/5, yHeart+50/5, fill=colour, outline=colour)



x = -40
y = 0
xx = 0
yy = 0
numHeart = 24
for sHeart in range(1, numHeart + 1):
    x = x + 40
    y = y + 40
    xx = 200
    yy = 300
    xHeart = randint(x, y)
    yHeart = randint(xx, yy)
    screen.create_oval(xHeart+10/5, yHeart+10/5, xHeart+30/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_oval(xHeart+25/5, yHeart+10/5, xHeart+45/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_polygon(xHeart+10/5, yHeart+23/5, xHeart+45/5, yHeart+23/5, xHeart+27.5/5, yHeart+50/5, fill=colour, outline=colour)
 
x = -95
y = 0
xx = 0
yy = 0
numHeart = 10
for sHeart in range(1, numHeart + 1):
    x = x + 95
    y = y + 95
    xx = 300
    yy = 400
    xHeart = randint(x, y)
    yHeart = randint(xx, yy)
    screen.create_oval(xHeart+10/5, yHeart+10/5, xHeart+30/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_oval(xHeart+25/5, yHeart+10/5, xHeart+45/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_polygon(xHeart+10/5, yHeart+23/5, xHeart+45/5, yHeart+23/5, xHeart+27.5/5, yHeart+50/5, fill=colour, outline=colour)

x = -190
y = 0
xx = 0
yy = 0
numHeart = 5
for sHeart in range(1, numHeart + 1):
    x = x + 190
    y = y + 190
    xx = 400
    yy = 500
    xHeart = randint(x, y)
    yHeart = randint(xx, yy)
    screen.create_oval(xHeart+10/5, yHeart+10/5, xHeart+30/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_oval(xHeart+25/5, yHeart+10/5, xHeart+45/5, yHeart+30/5, fill=colour, outline=colour)
    screen.create_polygon(xHeart+10/5, yHeart+23/5, xHeart+45/5, yHeart+23/5, xHeart+27.5/5, yHeart+50/5, fill=colour, outline=colour)


# Large Heart
screen.create_oval(450, 300, 800, 650, fill="seashell", outline="seashell")
screen.create_oval(700, 200, 1050, 550, fill="seashell", outline="seashell")
screen.create_polygon(550, 634, 1050, 400, 950, 775, fill="seashell")

# Bench

# Back Supporter
screen.create_rectangle(625, 475, 630, 550, fill="gainsboro", outline="gainsboro")
screen.create_rectangle(920, 475, 925, 550, fill="gainsboro", outline="gainsboro")
# Bench Shadow
screen.create_polygon(550, 650, 600, 575, 950, 575, 1000, 650, fill="#FFF09F", outline="#FFF09F", smooth=True)
# Bench Legs
screen.create_rectangle(610, 590, 625, 625, fill="white", outline="gray", width=3)
screen.create_rectangle(925, 590, 940, 625, fill="white", outline="gray", width=3)
# Bottom Bench Plank
screen.create_rectangle(590, 590, 960, 600, fill="lightskyblue", outline="lightskyblue")
screen.create_polygon(590, 590, 960, 590, 950, 550, 600, 550, fill="paleturquoise", outline="paleturquoise")
# Bottom Bench Outline
screen.create_line(625, 602, 925, 602, fill="gray", width=3)
screen.create_line(940, 602, 963, 602, fill="gray", width=3)
screen.create_line(961, 602, 961, 590, fill="gray", width=3)
screen.create_line(960, 590, 950, 548, fill="gray", width=3)
screen.create_line(950, 548, 600, 548, fill="gray", width=3)
screen.create_line(600, 548, 590, 590, fill="gray", width=3)
screen.create_line(590, 590, 590, 600, fill="gray", width=3)
screen.create_line(590, 602, 610, 602, fill="gray", width=3)
# Middle Bench Plank 1
screen.create_rectangle(610, 520, 940, 540, fill="white", outline="white")
# Middle Bench Plank 2
screen.create_rectangle(610, 510, 940, 490, fill="pink", outline="pink")
# Middle Bench Outline 1
screen.create_line(610, 520, 941, 520, fill="gray", width=3)
screen.create_line(610, 540, 941, 540, fill="gray", width=3)
screen.create_line(609, 519, 609, 542, fill="gray", width=3)
screen.create_line(941, 519, 941, 542, fill="gray", width=3)
# Middle Bench Outline 2
screen.create_line(610, 489, 941, 489, fill="gray", width=3)
screen.create_line(610, 512, 941, 512, fill="gray", width=3)
screen.create_line(609, 488, 609, 514, fill="gray", width=3)
screen.create_line(941, 488, 941, 514, fill="gray", width=3)
# Top Bench Plank
screen.create_polygon(610, 480, 610, 460, 942, 460, 940, 480, fill="paleturquoise", outline="paleturquoise")
screen.create_polygon(630, 455, 610, 460, 942, 460, 940, 455, fill="lightcyan", outline="lightcyan")
# Top Bench Outline
screen.create_line(610, 460, 630, 455, fill="gray", width=3)
screen.create_line(630, 455, 940, 455, fill="gray", width=3)
screen.create_line(940, 455, 945, 458, fill="gray", width=3)
screen.create_line(610, 482, 941, 482, fill="gray", width=3)
screen.create_line(609, 460, 609, 484, fill="gray", width=3)
screen.create_line(944, 458, 941, 484, fill="gray", width=3)
# Bench Screws
screen.create_oval(625, 468, 630, 473, fill="white", outline="white")
screen.create_oval(625, 498, 630, 503, fill="white", outline="white")
screen.create_oval(625, 528, 630, 533, fill="pink", outline="pink")
screen.create_oval(920, 468, 925, 473, fill="white", outline="white")
screen.create_oval(920, 498, 925, 503, fill="white", outline="white")
screen.create_oval(920, 528, 925, 533, fill="pink", outline="pink")



# Decides randomly where Hellp Kitty sits
xValue = 0
# randint(-100, 100)

# Hello Kitty

# Shadow
screen.create_oval(700+xValue, 550, 850+xValue, 595, fill="lightskyblue", outline="lightskyblue") 
# Stick
screen.create_line(835, 530, 865, 500, fill="brown", width=3)
# Arms + Hand
screen.create_oval(710+xValue, 525, 740+xValue, 550, fill="white", outline="black", width=5)
screen.create_polygon(750+xValue, 510, 725+xValue, 525, 750+xValue, 550, fill="darkgreen", outline="black", width=5)
screen.create_oval(840+xValue, 525, 810+xValue, 550, fill="white", outline="black", width=5)
screen.create_polygon(800+xValue, 510, 825+xValue, 525, 800+xValue, 550, fill="darkgreen", outline="black", width=5)
# Body
screen.create_polygon(775+xValue, 460, 825+xValue, 560, 810+xValue, 580, 740+xValue, 580, 725+xValue, 560, fill="darkgreen", outline="black", width=6)
screen.create_rectangle(750+xValue, 560, 800+xValue, 580, fill="white", width=5)
# Lined Underclothing
x=750+xValue
for lines in range(1, 10):
    x=x+5
    y=563
    xx=x
    yy=578
    screen.create_line(x, y, xx, yy, fill="darkgreen", width=4)

# Buttons
y=530
yy=535
for buttons in range(1, 4):
    x=770+xValue
    y=y+7
    xx=775+xValue
    yy=yy+7
    screen.create_oval(x, y, xx, yy, fill="darkgreen", outline="yellow",)

# Fold
screen.create_line(780+xValue, 535, 780+xValue, 560, width=5)
# Lined Underclothing + Collar
screen.create_oval(760+xValue, 505, 790+xValue, 535, fill="white", width=5)
screen.create_line(765+xValue, 510, 765+xValue, 529, fill="darkgreen", width=4)
screen.create_line(770+xValue, 508, 770+xValue, 533, fill="darkgreen", width=4)
screen.create_line(775+xValue, 508, 775+xValue, 533, fill="darkgreen", width=4)
screen.create_line(780+xValue, 508, 780+xValue, 533, fill="darkgreen", width=4)
screen.create_line(785+xValue, 508, 785+xValue, 533, fill="darkgreen", width=4)
screen.create_oval(760+xValue, 505, 790+xValue, 535, width=5)
screen.create_oval(760+xValue, 510, 790+xValue, 525, fill="white", width=2)
# Foot
screen.create_oval(715+xValue, 535, 760+xValue, 585, fill="white", width=5)
screen.create_oval(790+xValue, 535, 835+xValue, 585, fill="white", width=5)
# Ears
screen.create_polygon(700+xValue, 390, 730+xValue, 490, 860+xValue, 490, fill="white", outline="black", width=6, smooth=True)
screen.create_polygon(850+xValue, 390, 820+xValue, 490, 690+xValue, 490, fill="white", outline="black", width=6, smooth=True) 
# Face
screen.create_polygon(710+xValue, 422, 840+xValue, 422, 840+xValue, 517, 710+xValue, 517, fill="white", outline="black", width=6, smooth=True)
screen.create_oval(769+xValue, 485, 784+xValue, 495, fill="yellow", outline="black", width=4)
# Eyes
screen.create_oval(735+xValue, 472, 745+xValue, 485, fill="black", outline="black")
screen.create_oval(805+xValue, 472, 815+xValue, 485, fill="black", outline="black")
# Ear pt.2
screen.create_oval(717+xValue, 424, 767+xValue, 443, fill="white", outline="white")
screen.create_oval(783+xValue, 424, 833+xValue, 443, fill="white", outline="white") 
# Left Wiskers
screen.create_line(720+xValue, 480, 705+xValue, 480, 700+xValue, 485, width=4, smooth=True)
screen.create_line(722+xValue, 486, 705+xValue, 490, 706+xValue, 495, width=4, smooth=True)
screen.create_line(724+xValue, 492, 710+xValue, 505, width=4, smooth=True)
# Right Wiskers
screen.create_line(830+xValue, 480, 845+xValue, 480, 850+xValue, 485, width=4, smooth=True)
screen.create_line(828+xValue, 486, 845+xValue, 490, 844+xValue, 495, width=4, smooth=True)
screen.create_line(826+xValue, 492, 840+xValue, 505, width=4, smooth=True)
# Hair Pin
screen.create_polygon(820+xValue, 435, 775+xValue, 455, 775+xValue, 415, fill="pink", outline="black", width=3, smooth=True)
screen.create_polygon(800+xValue, 435, 845+xValue, 455, 845+xValue, 415, fill="pink", outline="black", width=3, smooth=True)
screen.create_oval(795+xValue, 430, 825+xValue, 440, fill="pink", width=2)
screen.create_oval(800+xValue, 425, 820+xValue, 445, fill="pink", width=2)
# Text
screen.create_text(275, 600, fill="deep pink", font="Comic 40", text="Hello Kitty")
screen.create_text(240, 640, fill="deep pink", font="Comic 20", text="By: Dennis P")
screen.update

# 865, 500

def graphics():
    frames = 10**10
    
    for frameCount in range(0, frames):
        # Oval Parameters
        ovalx1 = 860
        ovaly1 = 495
        ovalx2 = 870
        ovaly2 = 505
        screen.create_oval(ovalx1, ovaly1, ovalx2, ovaly2, fill="yellow", outline="yellow")
        screen.update()
        sleep(0.05)
        

graphics()












