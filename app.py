import time
from graphics import*

String1 = '''Choose your character to play this dragon fighting, cave-exploring adventure: the mage(1), the 
knight(2),  and generic dude(3)! The mage(1), with their mastery of spells and arcane arts, is a 
powerful force to be reckoned with, able to decimate enemies with a single wave of their hand. The 
knight(2), with their heavy armor and trusty sword, is a formidable warrior, able to charge into 
battle and withstand the toughest of blows. The normal man(3), while lacking in magical or combat 
abilities, has a unique set of skills and knowledge that may prove valuable in unexpected ways \n'''
for char in String1:
    print(char, end="")
    time.sleep(.00)



#Character Selection
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
elif choice == "2":
    win1 = GraphWin("Window1", 500, 500)
    win1.setBackground(color_rgb(0, 0, 0))

    img = Image(Point(250, 250), "knight.gif")
    img.draw(win1)

    txt = Text(Point(250, 420), "You have chosen the Knight!\nClick anywhere to continue")
    txt.setTextColor('white')
    txt.draw(win1)

    win1.getMouse()
    win1.close()
elif choice == "3":
    win1 = GraphWin("Window1", 500, 500)
    win1.setBackground(color_rgb(0, 0, 0))

    img = Image(Point(250, 250), "generic_dude.gif")
    img.draw(win1)

    txt = Text(Point(250, 420), "You have chosen the Generic Dude!\nClick anywhere to continue")
    txt.setTextColor('white')
    txt.draw(win1)

    win1.getMouse()
    win1.close()





String2 = '''As you enter the dimly lit shop, a faint aroma of herbs and incense fills the air. Shelves 
line the walls, crammed with exotic-looking objects of all shapes and sizes. In the center of the room, a large 
wooden table is covered with a variety of items.You walk over to the table and examine the wares. A small vial 
filled with a shimmering red liquid catches your eye - a health potion. Beside it, a rolled-up map is spread out, 
showing the dreary paths inside the cave, Skull Cavern. And to the far right, a fine letter with a seal, a contract
of knight welling to slay any monster whose path may cross his. Will you buy any of the items before you?\n'''
for char in String2:
    print(char, end="")
    time.sleep(.00)

shopchoice = input("Yes or No\n")

if shopchoice == "Yes" or shopchoice == "yes":
#messing around with shapes (don't use)
    win2 = GraphWin("Window2", 500, 500)

    win2.setBackground('grey')

    oval = Oval(Point(190, 100), Point(310, 145))
    oval.setOutline('black')
    oval.setFill(color_rgb(92, 75, 51))
    oval.draw(win2)
    oval.setWidth(5)

    rect = Rectangle(Point(210, 140), Point(290, 210))
    rect.setOutline('black')
    rect.setFill('white')
    rect.draw(win2)
    rect.setWidth(5)

    cir = Circle(Point(250, 300), 100)
    cir.setOutline('black')
    cir.setFill('red')
    cir.setWidth(5)
    cir.draw(win2)

    txt = Text(Point(250, 420), "Health Potion (50g)")
    txt.draw(win2)

    win2.getMouse()
    win2.close()

if shopchoice == "No" or shopchoice == "no":
    win2 = GraphWin("Window2", 500, 500)
    win2.setBackground('black')

    death = Image(Point(250,250),"death.gif")
    death.draw(win2)

    win2.getMouse()
    win2.close()
