import time
from graphics import*

String = '''Choose your character to play this dragon fighting, cave-exploring adventure: the mage(1), the 
knight(2),  and generic dude(3)! The mage(1), with their mastery of spells and arcane arts, is a 
powerful force to be reckoned with, able to decimate enemies with a single wave of their hand. The 
knight(2), with their heavy armor and trusty sword, is a formidable warrior, able to charge into 
battle and withstand the toughest of blows. The normal man(3), while lacking in magical or combat 
abilities, has a unique set of skills and knowledge that may prove valuable in unexpected ways \n'''
for char in String:
    print(char, end="")
    time.sleep(.00)

choice = input("1,2,3\n")
if choice == "1":
    win1 = GraphWin("Window1",500,500)
    win1.setBackground(color_rgb(0,0,0))

    img = Image(Point(250,250), "mage.gif")
    img.draw(win1)

    txt = Text(Point(250,420), "You have chosen the Mage!\nClick anywhere to continue")
    txt.setTextColor('white')
    txt.draw(win1)

    win1.getMouse()
    win1.close()

win = GraphWin("MyWindow", 500, 500)

win.setBackground('grey')

oval = Oval(Point(190, 100), Point(310, 145))
oval.setOutline('black')
oval.setFill(color_rgb(92, 75, 51))
oval.draw(win)
oval.setWidth(5)

rect = Rectangle(Point(210, 140), Point(290, 210))
rect.setOutline('black')
rect.setFill('white')
rect.draw(win)
rect.setWidth(5)

cir = Circle(Point(250, 300), 100)
cir.setOutline('black')
cir.setFill('red')
cir.setWidth(5)
cir.draw(win)

txt = Text(Point(250, 420), "Health Potion (50g)")
txt.draw(win)

win.getMouse()
win.close()
