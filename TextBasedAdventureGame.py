import random

###Player Class

class Player:
    def __init__(self, nickName, health=100, hasSword=False, hasShield=False, notDead=True, restartGame="y"):
        self.nickName = nickName
        self.health = 40
        self.hasSword = hasSword
        self.hasShield = hasShield
        self.notDead = notDead
        self.restartGame = restartGame

    def showStats(self):
        print("Health: ", self.health)
        if self.hasShield is True and self.hasSword is True:
            print("\nInventory:")
            print("1. Sword")
            print("2. Shield\n")
        elif self.hasShield is True and self.hasSword is False:
            print("\nInventory:")
            print("1.Shield\n")
        elif self.hasShield is False and self.hasSword is True:
            print("\nInventory:")
            print("1.Sword\n")
        else:
            print("\nInventory is Empty\n")
        
    def getWeapons(self):
        self.hasSword = True
        self.hasShield = True
        # print(self.hasSword)
        # print(self.hasShield)

    def decHealth(self):
        lostHealth = random.randint(1, 21)
        self.health -= lostHealth

        if(self.health < 1):
            self.Dead(self.restartGame)

    def attackEnemy(self):
        self.decHealth()

        self.showStats()

    def powerUp(self):
        self.health += 10
        if self.health > 100:
            self.health = 100

    def Dead(self, restartGame):
        self.notDead = False

        print("\nRestart Game?(y/n): ")
        self.restartGame = input()

        if self.restartGame == "y" or self.restartGame == "Y":
            self.notDead = True
        else:
            exit()

        print()
    
    def isDead(self):
        return self.notDead

def Game():
    print("\nEnter Name: ")
    name = input()
    player = Player(name)

    print("\nRules:-")
    print("Press number keys to choose the options")
    print("Press ctrl + z at any time to quit")
    print("Press 's' to start\n")

    keyPress = input()
    restartGame = "y"

    if keyPress == "s":
        while player.isDead():
            print("You are in a Dungeon of a Destroyd Castle. There is a door infront of you.") 
            print("You open the door and go out of the room. There is a room to your right and a corridor in front of you. What do you do?")
            print("1. Open the Door")
            print("2. Move Forward")

            choice = input()

            if choice == "2":
                print("\nYou move forward. A hoard of monsters chase you away. Game Over!\n")
                player.Dead(restartGame)

            elif choice == "1":
                print("You Enter the room. There is a chest inside. What do you do?")
                print("1. Open the Chest")
                print("2. Leave the room and continue")

                choice = input()
                if choice == "2":
                    print("You leave the room and continue the journey. A hoard of monsters chase you away. Game Over!\n")
                    player.Dead(restartGame)


                elif choice == "1":
                    print("You open the chest and find a sword and a shield. You pick up both and continue the journey.\n")
                    player.getWeapons()

                    print("You come accross a hoard of monsters. You kill them with your weapons, but lose some health. The enemies are dead(d.\n")
                    player.attackEnemy()
                    print("You Continue walking forward. You come across a junction.")
                    print("One path goes to the left, other staright and the other one towards right. Which path do yo take?\n")
                    print("1. Go Left")
                    print("2. Go Straight")
                    print("3. Go Right")

                    choice = input()

                    if choice == "1":
                        print("\nYou decide to turn Left. You are going straight, when you step on an unusual stone.")
                        print("Its a trap! You try to escape, but you come under a big boulder. Game Over!!!\n")
                        player.Dead(restartGame)
    

                    elif choice == "2":
                        print("\nYou decide to go straight. You come across a hoard of monsters. You fight and stands victorious, but lose some health.\n")
                        player.attackEnemy()

                        print("There is door in front of You. You go inside. There is a chest in front of you. You open it.")
                        print("You completed the objective for which you came here. You win!!")
                        break
            
                    elif choice == "3":
                        print("\nYou turn right. You find a Health powerup!!!")
                        print("You go back. What do you do?")

                        player.powerUp()
                        player.showStats()

                        print("1. Go Left")
                        print("2. Go Straight")

                        choice = input()

                        if choice == "1":
                            print("\nYou decide to turn Left. You are going straight, when you step on an unusual stone.")
                            print("Its a trap! You try to escape, but you come under a big boulder. Game Over!!!\n")
                            player.Dead(restartGame)
        

                        elif choice == "2":
                            print("\nYou decide to go straight. You come across a hoard of monsters. You fight and stand victorious, but lose some health.\n")
                            player.attackEnemy()

                            print("There is door in front of You. You go inside. There is a chest in front of you. You open it.")
                            print("You completed the objective for which you came here. You win!!")
                            break



def main():
    print(r"|````| |````\  \         / |`````` |`\     | ```|``` |     | |```\  |``````   |`````` |````| |^\     /^| |``````")
    print(r"|    | |     |  \       /  |       |  \    |    |    |     | |    | |         |       |    | |  \   /  | |      ")
    print(r"|----| |     |   \     /   |----   |   \   |    |    |     | |  _/  |----     |   __  |----| |   \_/   | |----  ")
    print(r"|    | |     |    \   /    |       |    \  |    |    |     | |  \   |         |     | |    | |         | |      ")
    print(r"|    | |____/      \_/     |______ |     \_|    |    |_____| |   \  |______   |_____| |    | |         | |______")
    Game()

main()