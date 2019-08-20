#!/usr/bon/python3

def showInstructions():

    print('''
            RPG GAME
            --------
            Commands:
            go [direction]
            get [item]
    ''')


def showStatus():
    print('-------------------------------------------')
    print(f"You are in the {currentRoom}")
    print("Inventory: " + str(inventory))
    if "item" in rooms[currentRoom]:
        print(f"You see a {rooms[currentRoom]['item']}")
    print("--------------------------------------------")

inventory = []

rooms = {
            'Hall' : {
                'south': 'Kitchen'
                },
                'Kitchen': {
                    'north': 'Hall'
                }
        }

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()
    move = ''
    while move == '':
        move = input("> ")

    move = move.lower().split()

#    'GO east"
#    ['go', 'east']

    if move[0] == 'go':
        if move [1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("you cannt go that way!")
    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(f"you just picked up {move[1]}!")
            del rooms[currentRoom]['item']

        else:
            print("You cannot pick that up!")

#main()

