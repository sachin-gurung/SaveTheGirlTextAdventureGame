# Sachin Gurung
def run_game():

    global direction_or_item

    # create a dictionary of rooms
    rooms = {
        'Great Room': {'east': 'Family Room', 'west': 'Kitchen', 'north': 'Bedroom 1', 'south': 'Bedroom 3'},
        'Bedroom 3': {'east': 'Basement', 'north': 'Great Room', 'item': 'Rice'},
        'Basement': {'west': 'Bedroom 3', 'item': 'Steak'},
        'Kitchen': {'east': 'Great Room', 'item': 'Broccoli'},
        'Family Room': {'west': 'Great Room', 'north': 'Recreation Room', 'item': 'Milk'},
        'Recreation Room': {'south': 'Family Room'},
        'Bedroom 1': {'south': 'Great Room', 'east': 'Bedroom 2', 'west': 'Bedroom 4', 'item': 'Banana'},
        'Bedroom 4': {'east': 'Bedroom 1', 'item': 'Chocolate'},
        'Bedroom 2': {'west': 'Bedroom 1'}
    }

    # start the player in the Hall
    current_room = 'Great Room'

    # create an inventory, an empty list
    inventory = []

    # define functions
    def show_instructions():
        # print a main menu and the commands
        print("Save the Girl - Text Adventure Game")
        print("Collect 6 items to win the game or get killed by the guard!!!")
        print("Move commands: go South, go North, go East, go West")
        print("To add to inventory: get 'item name'")

    def show_status():
        # print the player's current status
        print('-----------------------------------------')
        print('You are in the ' + current_room + '.')
        print('Inventory: ' + str(inventory))
        if "item" in rooms[current_room]:
            print('You see a ' + rooms[current_room]['item'])
        print('-----------------------------------------')

    show_instructions()

    # loop forever
    while True:
        show_status()

        # check if the player has won
        if len(inventory) == 6:
            print('You have collected all the items. You win!')
            break

        # check if the player has lost
        if current_room == 'Recreation Room' and len(inventory) < 6:
            print('You have been caught by the guard. You lose!')
            break

        if current_room == 'Bedroom 2' and len(inventory) < 6:
            print('You see a girl in the corner of the room. She looks very scared.\n'
                  'You talk to her: \n'
                  'Hello there! I am so glad I found you here. I am here to save you but I\'ll have to collect'
                  ' all the items first. I\'ll be back soon.')

        command = input("\nEnter a command (east, west, north, south, get [item], quit): ").lower()
        commands = command.split()

        if len(commands) == 2:
            action, direction_or_item = commands
        else:
            action = commands[0]

        if command == 'quit':
            print('Thanks for playing the game. Hope you enjoyed it.')
            break
        elif action == 'go' and direction_or_item in rooms[current_room]:
            current_room = rooms[current_room][direction_or_item]
        elif action == 'get' and 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == direction_or_item:
            inventory.append(rooms[current_room]['item'])
            print(rooms[current_room]['item'] + ' added to inventory.')
            del rooms[current_room]['item']
        else:
            print('Invalid command')



