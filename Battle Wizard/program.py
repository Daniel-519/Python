import random
import time

from actors import Wizard
from actors import Creature


def main():
    print_the_header()
    game_loop()


def print_the_header():
    print('=====================')
    print('    Battle Wizard')
    print('=====================')
    print()


def game_loop():
    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]
    # print(creatures)
    hero = Wizard('Gandolf', 75)
    while True:
        active_creature = random.choice(creatures)
        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around?")

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!')
        elif cmd == 'l':
            print("The wizard {} takes in the surroundings and sees...".format(hero.name))
            for c in creatures:
                print("* A {} of level {}".format(c.name, c.level))
        else:
            print("Ok, Existing game.... Bye!!!!")
            break
        if not creatures:
            print("You've defeated all the wizards, well done!")
            break


if __name__ == '__main__':
    main()
