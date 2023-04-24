import time
from graphics import*

intro = '''
Congratulations! The King has selected you to go on a quest to slay a mighty dragon! What class will you choose? 
(1) Mage
(2) Knight
(3) Generic Dude\n\n'''
for char in intro:
    print(char, end="")
    time.sleep(.03)



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


shop_prompt = '''\nHalt! You can't go empty handed! Before you depart, do you want to visit the shop?\n'''
for char in shop_prompt:
    print(char, end="")
    time.sleep(.03)

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
    win2 = GraphWin("Window2", 550, 550)
    win2.setBackground('black')

    death = Image(Point(250,250),"death.gif")
    death.draw(win2)

    win2.getMouse()
    win2.close()
