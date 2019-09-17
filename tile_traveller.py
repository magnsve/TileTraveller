# Tile TravellerIn this assignment, you work in groups of two students each and apply pair programing. Moreover, you need to use 
# git during the development of your solution.The assignment is to develop a computer game in which the player is located in a 
# certain tile in a grid. At each iteration, the program displays the directions for which there are adjacent tiles that the player 
# can travel to. The program only displays text, so you don’t actually draw the tile grid, but the program should behave as if the 
# player is in a 3x3 grid with open and closed walls as seen in the following image. Tile TravellerIn this assignment, you work in 
# groups of two students each and apply pair programing. Moreover, you need touse gitduring the development of your solution.The 
# assignment is to develop a computer game in which the player is located in a certain tile in a grid. At each iteration, the program 
# displays the directions for which there are adjacent tiles that the player can travel to. The program only displays text, so you 
# don’t actually draw the tile grid, but the program should behave as if the player is in a 3x3 grid with open and closed walls as 
# seen in the following image:The player starts in tile (1,1). At the beginning, and after each move selected by the player, the 
# program should print the player’s travel options. If there is an open wall in a direction, write that direction as a possible 
# travel direction.At each iteration, the player enters the first letter of the direction he/she wishes to travel, after which the 
# player should be located in another tile and the options for the new tile are then printed out.The player enters: 
#
# •n/N for north (up)
# •e/E for east (right)
# •s/S for south (down)
# •w/W for west (left)
# 
# If the player enters an invalid direction, the program prints “Not a valid direction!” and allows the player to enter the direction 
# again.For example, in tile (1,1) it’s only possible to move north. In tile (1,2), the possible moves are north, east and south, and 
# in tile (3,3) the valid moves are south and west.Tile (3,1) is the victory location. When the player enters this tile,the program s
# hould notify him/her of their victory and quit running

# Start with the algorithm.
# We start by defining a functon for the cells using if, elif for the 9 cells.
# We then ask for input from the user the function returns the updated cell value and repeats until finish.

cellvalue = 11
direction = ''

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

while cellvalue != 31:
    cellvalue = travel(cellvalue)
else: 
    print('Victory!')