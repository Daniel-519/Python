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

    hero = Wizard('Gandolf', 75)

    while True:
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            print()
        elif cmd == 'r':
            print()
        elif cmd == 'l':
            print()
        else:
            print("Ok, Existing game.... Bye!!!!")
            break


if __name__ == '__main__':
    main()
