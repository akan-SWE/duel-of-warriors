#!/usr/bin/python3
import random


class Warriors:
    """Defines a warrior for battle simulation.

    Attributes:
        name (str): Name of the warrior.
        health (int): Health points of the warrior.
        maxAttacks (int): Maximum damage a warrior can deal in an attack.
        maxBlock (int): Maximum damage a warrior can block.

    Methods:
        attack(): Generates a random attack damage.
        block(): Generates a random block amount.
        __str__(): Returns the name of the warrior.

    Properties:
        name (getter, setter): Gets or sets the name of the warrior.
        health (getter, setter): Gets or sets the health of the warrior.
    """
    maxAttacks = 10
    maxBlocks = 8

    def __init__(self, name='player', health=10):
        self.name = name
        self.health = health

    def attack(self):
        return random.randrange(0, 2) * Warriors.maxAttacks + .5

    def block(self):
        return random.randrange(0, 2) * Warriors.maxBlocks + .5

    @property
    def health(self):
        return self.__health

    @property
    def name(self):
        return self.__name

    @health.setter
    def health(self, value):
        self.__health = value

    @name.setter
    def name(self, value):
        if not len(value):
            self.__name = 'id'+"".join(str(x) for x in
                                       random.choices(range(4), k=5))
        elif len(value) > 25:
            raise ValueError('string length of name is too '
                             'long (25 characters max)')
        else:
            self.__name = value

    def __str__(self):
        return {}.format(self.name)


class Battle:
    """Manages the battle interface for two warriors

    Attributes:
        warriors (list): A list containing warrior objects

    Methods:
        fight(): Initiates the battle between two warriors
        getAttackResults: Initiates the fight between the warriors
        __str__(): Returns a string representation of the objects
    """
    warriors = []

    def fight(self, warrior1, warrior2):
        i, damage = 0, 0
        Battle.warriors = [warrior1, warrior2]
        print(self, end='\n\n')
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print(f"{warrior1.name} wins!")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print(f"{warrior2.name} wins!")
                break

            print('')
            i += 1

    def __str__(self):
        name1 = Battle.warriors[0].name
        name2 = Battle.warriors[1].name
        return ('*' * 100 + '\n' + ('\t\t{} [H:{}]\t\t\tvs'
                                    '\t\t\t\t{:} [H:{}]')
                .format(name1, Battle.warriors[0].health,
                        name2, Battle.warriors[1].health))

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        from math import ceil

        attackAmount = warriorA.attack()
        blockAmount = warriorB.block()

        damage2WarriorB = ceil(attackAmount - blockAmount)
        warriorB.health -= 0 if damage2WarriorB < 0 else damage2WarriorB

        print(f"\n{warriorA.name} attacks {warriorB.name} deals "
              f"{damage2WarriorB} damage")
        print(f"{warriorB.name} is down to {warriorB.health} health")

        return "Game Over" if warriorB.health <= 0 else "Game On"


def main():
    """ Starts the program
    :return: None
    """

    name1 = input('Choose a name for the first warrior ')
    name2 = input('Choose a name for the second warrior ')

    w1 = Warriors(name1, 15)
    w2 = Warriors(name2, 15)

    b = Battle()
    b.fight(w1, w2)


main()
