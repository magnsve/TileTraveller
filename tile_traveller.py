# magnus10 og liljas17

# For project description see Assignment 8 in Mimir.

# Start with the algorithm.
# We start by defining all cells and their properties.
# Next we create a function that asks for user input and validates it.

import random
INIT = (1,1)
NORTH = 'n'
SOUTH = 's'
WEST = 'w'
EAST = 'e'

def print_directions(direction_string):
    print("You can travel: ", end='')
    first = True
    for char in direction_string:
        if not first:
            print(" or ", end='')
        if char == NORTH:
            print("(N)orth",end = '')
        if char == EAST:
            print("(E)ast", end = '')
        if char == SOUTH:
            print("(S)outh", end= '')
        if char == WEST:
            print("(W)est", end = '')
        first = False
    print('.')


def cell(coordinates):    
    ''' This function defines each cell and it's properties '''    
    cells = [[(1,1),NORTH], [(1,2),NORTH+EAST+SOUTH], [(1,3),EAST+SOUTH], [(2,3),EAST+WEST], [(3,3),SOUTH+WEST], [(3,2),NORTH+SOUTH], [(3,1),NORTH], [(2,2),SOUTH+WEST], [(2,1),NORTH]]
    for element in cells:
        element_coordinates = element[0]
        if element_coordinates == coordinates:
            directions = element[1]
    return directions

def is_valid(user_input,directions):
    '''Validation for user input'''
    for ch in directions:
        if ch == user_input:
            result = True
            break
    else: 
        print('Not a valid direction!')
        result = False

    return result

def travel(cellvalue, coins_before, tracker):
    ''' Prints out current positon, gets user input and updates cell values '''
    x, y = cellvalue
    possible_directions = cell(cellvalue)
    coins_after = pull_lever(cellvalue, coins_before)    
    legal_move = False
    
    while legal_move == False:        
        print_directions(possible_directions)
        print('Direction: ',end = '')
        dir = random.choice([NORTH,EAST,SOUTH,WEST])
        print(dir)
        dir = dir.lower()
        legal_move = is_valid(dir,possible_directions)         
        tracker += 1

    if dir == NORTH:
        y += 1
    elif dir == SOUTH:
        y -= 1
    elif dir == EAST:
        x += 1
    elif dir == WEST:
        x-= 1
    
    cellvalue = (x,y)
    
    return cellvalue, coins_after, tracker

def pull_lever(cellvalue, coins):
    cells = [[(1,1), False], [(1,2), True], [(1,3), False], [(2,3), True], [(3,3), False], [(3,2), True], [(3,1), False], [(2,2), True], [(2,1), False]]
    for element in cells:
        element_lever = element[0]
        if element_lever == cellvalue:
            lever = element[1]            
            if lever == True:
                print('Pull a lever (y/n): ', end='')
                pull_lever = random.choice(['y','n'])
                print(pull_lever)
                pull_lever = pull_lever.lower()                
                if pull_lever == 'y':
                    coins += 1
                    print('You received 1 coin, your total is now {}.'.format(coins))

    return coins

def main(first_cell):    
    random.seed(int(input('Input seed: ')))
    cellvalue = first_cell
    total_coins = 0
    tracker = 0
    while cellvalue != (3,1):
        cellvalue, total_coins, tracker = travel(cellvalue, total_coins, tracker)
    else: 
        print('Victory! Total coins {}. Moves {}.'.format(total_coins,tracker))

    play_again = input('Play again (y/n): ')
    play_again = play_again.lower()    
    
    return play_again

# Now we can play the game. Start by setting start position to 1,1.

play_again = 'y'

while play_again == 'y':
    play_again = main(INIT)