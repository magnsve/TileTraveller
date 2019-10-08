# magnus10 og liljas17

# For project description see Assignment 8 in Mimir.

# Start with the algorithm.
# We start by defining all cells and their properties.
# Next we create a function that asks for user input and validates it.

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
    cells = [[(1,1),NORTH], [(1,2),NORTH+SOUTH+EAST], [(1,3),EAST+SOUTH], [(2,3),EAST+WEST], [(3,3),WEST+SOUTH], [(3,2),NORTH+SOUTH], [(3,1),NORTH], [(2,2),WEST+SOUTH], [(2,1),NORTH]]
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

def travel(cellvalue, coins_before):
    ''' Prints out current positon, gets user input and updates cell values '''
    x, y = cellvalue
    possible_directions = cell(cellvalue)
    coins_after = pull_lever(cellvalue, coins_before)
    print_directions(possible_directions)
    legal_move = False
    
    while legal_move == False:        
        dir = input('Direction: ')
        dir = dir.lower()
        legal_move = is_valid(dir,possible_directions) 
        

    if dir == NORTH:
        y += 1
    elif dir == SOUTH:
        y -= 1
    elif dir == EAST:
        x += 1
    elif dir == WEST:
        x-= 1
    
    cellvalue = (x,y)
    
    return cellvalue, coins_after

def pull_lever(cellvalue, coins):
    cells = [[(1,1), False], [(1,2), True], [(1,3), False], [(2,3), True], [(3,3), False], [(3,2), True], [(3,1), False], [(2,2), True], [(2,1), False]]
    for element in cells:
        element_lever = element[0]
        if element_lever == cellvalue:
            lever = element[1]            
            if lever == True:
                pull_lever = input('Pull a lever (y/n):')
                pull_lever = pull_lever.lower()                
                if pull_lever == 'y':
                    coins += 1
                    print('You received 1 coin, your total is now {}.'.format(coins))

    return coins
# Now we can play the game. Start by setting start position to 1,1.
cellvalue = (1,1)
total_coins = 0

while cellvalue != (3,1):
    cellvalue, total_coins = travel(cellvalue, total_coins)
else: 
    print('Victory! Total coins {}.'.format(total_coins))