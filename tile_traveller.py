# magnus10 og liljas17

# For project description see Assignment 8 in Mimir.

# Start with the algorithm.
# We start by defining all cells and their properties.
# Next we create a function that asks for user input and validates it.

def cell(x,y):    
    ''' This function defines each cell and it's properties '''

    if x == 1 and y == 1:
        direction = 'nN' 
        print('You can travel: (N)orth.')
    elif x == 1 and y == 2:
        direction = 'nseNSE'
        print('You can travel: (N)orth or (E)ast or (S)outh.')
    elif x == 1 and y == 3:
        direction = 'esES'
        print('You can travel: (E)ast or (S)outh.')
    elif x == 2 and y == 3:
        direction = 'ewEW'
        print('You can travel: (E)ast or (W)est.')
    elif x == 3 and y == 3:
        direction = 'wsWS'
        print('You can travel: (S)outh or (W)est.')
    elif x == 3 and y == 2:
        direction = 'nsNS'
        print('You can travel: (N)orth or (S)outh.')
    elif x == 3 and y == 1:
        direction = 'nN'
        print('Victory!')
    elif x == 2 and y == 2:
        direction = 'wsWS'
        print('You can travel: (W)est or (S)outh.')
    elif x == 2 and y == 1:
        direction = 'nN'
        print('You can travel: (N)orth.')

    return direction

def is_valid(user_input,definition):
    '''Validation for user input'''

    for ch in definition:
        if ch == user_input:
            result = True
            break
    else: 
        print('Not a valid direction!')
        result = False

    return result

def travel(cellvalue):
    ''' Prints out current positon, gets user input and updates cell values '''
    x = int(cellvalue/10)
    y = cellvalue%10
    possible_directions = cell(x,y)
    legal_move = False

    while legal_move == False:
        dir = input('Direction: ')
        legal_move = is_valid(dir,possible_directions) 

    if dir == 'n' or dir =='N':
        y += 1
    elif dir == 's' or dir == 'S':
        y -= 1
    elif dir == 'e' or dir == 'E':
        x += 1
    elif dir == 'w' or dir == 'W':
        x-= 1

    cellvalue = int(str(x)+str(y))

    return cellvalue


# Now we can play the game. Start by setting start position to 1,1.
cellvalue = 11

while cellvalue != 31:
    cellvalue = travel(cellvalue)
else: 
    print('Victory!')