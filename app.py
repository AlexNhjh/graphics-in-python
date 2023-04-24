import time
from graphics import*

intro = '''
Congratulations! The King has selected you to go on a quest to slay a mighty dragon! What class will you choose? 
(1) Mage
(2) Knight
(3) Generic Dude\n\n'''
for char in intro:
    print(char, end="")
    time.sleep(.00)

death = Image(Point(250,250),"death.gif")

#Character Selection
choice = input("1, 2, 3\n")
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

#Shop time
shop_prompt = '''\nHalt! You can't go empty handed! Before you depart, do you want to visit the shop?\n'''
for char in shop_prompt:
    print(char, end="")
    time.sleep(.00)

shopchoice = input("Yes or No\n")

if shopchoice == "Yes" or shopchoice == "yes":
    total_gold = 100


    win2 = GraphWin("Window2", 600, 600)
    win2.setBackground('black')

    shopkeeper = Image(Point(400,150),"shopkeeper.gif")
    shopkeeper.draw(win2)
    shopkeeper_prompt = Text(Point(150,150),"Welcome Traveller! \nWhat would you like to purchase")
    shopkeeper_prompt.setTextColor('white')
    shopkeeper_prompt.draw(win2)

#Health Potion section
    healthPotion = Image(Point(100,420),"health.gif")
    healthPotion.draw(win2)
    health_prompt = Text(Point(100, 500), "Health Potion (50g)\nType 1 to Confirm")
    health_prompt.setTextColor('white')
    health_prompt.draw(win2)
#Map
    map = Image(Point(300,420),"map.gif")
    map.draw(win2)
    map_prompt = Text(Point(300,500), "Map (100g)\nType 2 to Confirm")
    map_prompt.setTextColor('white')
    map_prompt.draw(win2)
#Donkey
    donkeyimg = Image(Point(500,420),"donkey.gif")
    donkeyimg.draw(win2)
    donkey_prompt = Text(Point(500,500), "Donkey (100g)\nType 3 to Confirm")
    donkey_prompt.setTextColor('white')
    donkey_prompt.draw(win2)

    total_gold = Text(Point(300,570),"You Have:" +str(total_gold))
    total_gold.setTextColor('gray')
    total_gold.draw(win2)

    shopItem = input("\n1, 2, 3\n")



elif shopchoice == "No" or shopchoice == "no":
    win2 = GraphWin("Window2", 550, 550)
    win2.setBackground('black')

    death.draw(win2)

    win2.getMouse()
    win2.close()

if shopItem == 1:
    print("You have purchased a health potion!")
    win2.getMouse()
    win2.close()
if shopItem == 2:
    print("You have purchased a Map!")
    win2.getMouse()
    win2.close()
if shopItem == 3:
    print("You have purchased a donkey!")
    win2.getMouse()
    win2.close()
