###Player Class

class Player:
    def __init__(self, nickName, health=100, hasSword=False, hasShield=False, powerUps = [], notDead=True):
        self.nickName = nickName
        self.health = 100
        self.hasSword = hasSword
        self.hasShield = hasShield
        self.powerUps = powerUps
        self.notDead = notDead

    def showStats(self):
        print("Health: ", self.health)
        if self.hasShield is True and self.hasSword is True:
            print("Inventory:")
            print("1. Sword")
            print("2. Shield")
        elif self.hasShield is True and self.hasSword is False:
            print("Inventory:")
            print("1.Shield")
        elif self.hasShield is False and self.hasSword is True:
            print("Inventory:")
            print("1.Sword")
        else:
            print("Inventory is Empty")

        print("PowerUps Used: ")

        for i in self.powerUps:
            if i is "health":
                print("health: Restores Health")
            elif i is "oneHitKill":
                print("oneHitKill: Kills enemy with one hit, can be used only once with no health loss")
            else:
                print("No Power Ups used yet!")
                break
        
    def getWeapons(self):
        self.hasSword = True
        self.hasShield = True
        # print(self.hasSword)
        # print(self.hasShield)

    def decHealth(self):
        self.health -= 5

        if(self.health < 1):
            self.Dead()

    def attackEnemy(self):
        self.decHealth()

    def powerUp(self, pickUps):
        if pickUps is "health":
            self.powerUps.append(pickUps)
            self.health = 100
        elif pickUps is "oneHitKill":
            self.powerUps.append(pickUps)

    def Dead(self):
        self.notDead = False
    
    def isDead(self):
        return self.notDead


def Game():
    print("Enter Name: ")
    name = input()
    player = Player(name)

    print("Rules:-")
    print("Press number keys to choose the options")
    print("Press i to see the inventory and the power ups used")
    print("Press ctrl + z at any time to quit")
    print("Press 's' to start")

    keyPress = input()

    if keyPress == "s":
        while (player.isDead()):
            print("You are in a Dungeon of a Destroyd Castle. There is a door infront of you.") 
            print("You open the door and go out of the room. There is a room to your right and a corridor in front of you. What do you do?")
            print("1. Open the Door")
            print("2. Move Forward")

            choice = input()
            if choice == "2":
                print("You move forward. A hoard of monsters chase you away. Game Over!")
                player.Dead()

            elif choice == "1":
                print("You Enter the room. There is a chest inside. What do you do?")
                print("1. Open the Chest")
                print("2. Leave the room and continue")

                choice1 = input()
                if choice1 == "2":
                    print("You leave the room and continue the journey. A hoard of monsters chase you away. Game Over!")
                    player.Dead()

                elif choice1 == "1":
                    print("You open the chest and find a sword and a shield. You pick up both and continue the journey.")
                    player.getWeapons()

                    print("You come accross a hoard of monsters. You kill them with your weapons, but lose some health.")
                    player.attackEnemy()
                    break
                    
                elif choice1 == "i":
                    player.showStats()
            
            elif choice == "i":
                player.showStats()

def main():
    Game()

main()