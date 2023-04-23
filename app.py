import time
from graphics import*

String = "Choose your character to play this dragon fighting, cave-exploring adventure: the mage(1), the \n" \
         "knight(2),  and generic dude(3)! The mage(1), with their mastery of spells and arcane arts, is a \n"\
         "powerful force to be reckoned with, able to decimate enemies with a single wave of their hand. The \n"\
         "knight(2), with their heavy armor and trusty sword, is a formidable warrior, able to charge into \n" \
         "battle and withstand the toughest of blows. The normal man(3), while lacking in magical or combat \n"\
         "abilities, has a unique set of skills and knowledge that may prove valuable in unexpected ways \n"
for char in String:
    print(char, end="")
    time.sleep(.00)

input("1,2,3\n")

win1 = GraphWin("Window1",500,500)
win1.setBackground(color_rgb(0,0,0))

img = Image(Point(250,250), "mage.gif")
img.draw(win1)

txt = Text(Point(250,420), "You have chosen the Mage!")
txt.setTextColor('white')
txt.draw(win1)

win1.getMouse()
win1.close()


