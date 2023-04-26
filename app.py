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
def death():
    win2 = GraphWin("Window2", 550, 550)
    win2.setBackground('black')
    death = Image(Point(250, 250), "death.gif")
    death.draw(win2)

    win2.getMouse()
    win2.close()

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
def shop():
    shop_prompt = '''\nHalt! You can't go empty handed! Before you depart, do you want to visit the shop?\n'''
    for char in shop_prompt:
        print(char, end="")
        time.sleep(.00)

    shopchoice = input("Yes or No\n")


    if shopchoice == "Yes" or shopchoice == "yes":
        total_goldAmount = 100


        win2 = GraphWin("Window2", 600, 600)
        win2.setBackground('black')

        shopkeeper = Image(Point(400,150),"shopkeeper.gif")
        shopkeeper.draw(win2)
        shopkeeper_prompt = Text(Point(150,150),"Welcome Traveller! \n\nWhat would you like to purchase \nfor your travels?")
        shopkeeper_prompt.setTextColor('white')
        shopkeeper_prompt.draw(win2)

    #Health Potion section
        healthPotion = Image(Point(100,420),"health.gif")
        healthPotion.draw(win2)
        health_prompt = Text(Point(100, 500), "Health Potion (50g)\nType 1 to Purchase")
        health_prompt.setTextColor('white')
        health_prompt.draw(win2)
    #Map
        map = Image(Point(300,420),"map2.gif")
        map.draw(win2)
        map_prompt = Text(Point(300,500), "Map (50g)\nType 2 to Purchase")
        map_prompt.setTextColor('white')
        map_prompt.draw(win2)
    #Donkey
        donkeyimg = Image(Point(500,420),"donkey.gif")
        donkeyimg.draw(win2)
        donkey_prompt = Text(Point(500,500), "Donkey (100g)\nType 3 to Purchase")
        donkey_prompt.setTextColor('white')
        donkey_prompt.draw(win2)

        total_gold = Text(Point(300,570),"You Have:" +str(total_goldAmount) +"g")
        total_gold.setTextColor('gray')
        total_gold.draw(win2)

        shopItem = input("\n1, 2, 3\n")

        if shopItem == "1":
            total_goldAmount = total_goldAmount - 50
            total_gold.setText("You Have: " + str(total_goldAmount) + "g")

            shop_confirm = Text(Point(300,545),"You Have purchased a Health Potion! Click to continue")
            shop_confirm.setTextColor('white')
            shop_confirm.draw(win2)

            healthPotion.undraw()
            health_prompt.undraw()

            outOfStockImg = Image(Point(100, 420), "out_of_stock.gif")
            outOfStockImg.draw(win2)

            outOfStockTxt = Text(Point(100,500), "Out of Stock")
            outOfStockTxt.setTextColor('white')
            outOfStockTxt.draw(win2)

            total_gold = Text(Point(300, 570), "You Have:" + str(total_goldAmount) + "g")
            total_gold.setTextColor('gray')
            total_gold.draw(win2)



        elif shopItem == "2":
            total_goldAmount = total_goldAmount - 50
            total_gold.setText("You Have: " + str(total_goldAmount) + "g")

            shop_confirm = Text(Point(300, 545), "You Have purchased a Map! Click to continue")
            shop_confirm.setTextColor('white')
            shop_confirm.draw(win2)

            map.undraw()
            map_prompt.undraw()

            outOfStockImg = Image(Point(300, 420), "out_of_stock.gif")
            outOfStockImg.draw(win2)

            outOfStockTxt = Text(Point(300, 500), "Out of Stock")
            outOfStockTxt.setTextColor('white')
            outOfStockTxt.draw(win2)

            total_gold = Text(Point(300, 570), "You Have:" + str(total_goldAmount) + "g")
            total_gold.setTextColor('gray')
            total_gold.draw(win2)

        elif shopItem == "3":
            total_goldAmount = total_goldAmount - 100
            total_gold.setText("You Have: " + str(total_goldAmount) + "g")

            shop_confirm = Text(Point(300, 545), "You Have purchased a Donkey! Click to continue")
            shop_confirm.setTextColor('white')
            shop_confirm.draw(win2)

            donkeyimg.undraw()
            donkey_prompt.undraw()

            outOfStockImg = Image(Point(500, 420), "out_of_stock.gif")
            outOfStockImg.draw(win2)

            outOfStockTxt = Text(Point(500, 500), "Out of Stock")
            outOfStockTxt.setTextColor('white')
            outOfStockTxt.draw(win2)

            total_gold = Text(Point(300, 570), "You Have:" + str(total_goldAmount) + "g")
            total_gold.setTextColor('gray')
            total_gold.draw(win2)

        win2.getMouse()
        win2.close()


    elif shopchoice == "No" or shopchoice == "no":
        death()

#First Cave
def cave():
    cave1Window = GraphWin("First Cave",700,500)
    cave1Window.setBackground('black')

    cave1Prompt = Text(Point(350,450),"cave text (idk what)")
    cave1Prompt.setTextColor('white')
    cave1Prompt.draw(cave1Window)

    cave1Image = Image(Point(350,250),"cave.gif")
    cave1Image.draw(cave1Window)

    cave1Window.getMouse()
    cave1Window.close()

#2nd Cave
def cave2():
    cave2Window = GraphWin("2nd Cave",450,450)
    cave2Window.setBackground('black')

    cave2Prompt = Text(Point(225,425),"cave text (idk what)")
    cave2Prompt.setTextColor('white')
    cave2Prompt.draw(cave2Window)

    cave2Image = Image(Point(225,210),"cave2.gif")
    cave2Image.draw(cave2Window)

    cave2Window.getMouse()
    cave2Window.close()

#Dragon
def dragon():
    dragonWindow = GraphWin("Dragon", 500, 460)
    dragonWindow.setBackground('black')
    dragonPrompt = Text(Point(250, 425), "oh a dragon das crazy")
    dragonPrompt.setTextColor('white')
    dragonPrompt.draw(dragonWindow)
    dragonImage = Image(Point(250, 200), "dragon.gif")
    dragonImage.draw(dragonWindow)
    dragonWindow.getMouse()
    dragonWindow.close()

#Cave Entrance
def cave_entrance():
    cave_entranceWindow = GraphWin("Cave_Entrance", 500, 400)
    cave_entranceWindow.setBackground('black')

    cave_entracePrompt = Text(Point(250, 320), "The path seems to lead here.\nClick to continue")
    cave_entracePrompt.setTextColor('white')
    cave_entracePrompt.draw(cave_entranceWindow)

    cave_entraceImage = Image(Point(250, 175), "cave_entrance.gif")
    cave_entraceImage.draw(cave_entranceWindow)
    cave_entranceWindow.getMouse()
    cave_entranceWindow.close()

#Monster
def monster():
    monsterWindow = GraphWin("Monster", 500, 500)
    monsterWindow.setBackground('black')

    monsterImg = Image(Point(250, 250), "monster.gif")
    monsterImg.draw(monsterWindow)

    monsterPrompt =Text(Point(250,420),"A monster was guarding the entrance to the cave! \nWhat do you want to do?")
    monsterPrompt.setTextColor('white')
    monsterPrompt.draw(monsterWindow)

    monsterChoice = input('''\nType 1 to Fight\nType 2 to Run\n''')
    if monsterChoice == "1":
        killMonster = Text(Point(250,460),"After a fierce battle, you manage to kill the monster!\nClick to continue")
        killMonster.setTextColor('white')
        killMonster.draw(monsterWindow)

    elif monsterChoice == "2":
        death()

    monsterWindow.getMouse()
    monsterWindow.close()

#Dragon
def path():
    pathWindow = GraphWin("Path", 500, 470)
    pathWindow.setBackground('black')
    pathImg = Image(Point(250,250),"path.gif")
    pathImg.draw(pathWindow)

    pathPrompt =  "\nOn your journey, you come across a fork in the road. Where do you want to go?\n"
    for char in pathPrompt:
        print(char, end="")
        time.sleep(.03)

    pathChoice = input("Go left or right?\n")
    if pathChoice == "Left" or pathChoice == "left":
        cave_entrance()
        monster()
        cave()
    elif pathChoice == "Right" or pathChoice == "Right":
        pathWindow.getMouse()
        pathWindow.close()

        cave_entrance()
        monster()
        cave2()

    pathWindow.getMouse()
    pathWindow.close()

shop()
path()
dragon()
