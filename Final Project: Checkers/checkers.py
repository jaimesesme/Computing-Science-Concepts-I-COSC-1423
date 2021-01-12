import random
def view(pieces,title="",debug=False):
    """
    The top of the board is row 1 and the far left is column 1
    """
    board = [' ']*64 # consider the board in row-echelon form

    # a swap specific to the board display and the interpretation of 
    # "a", i.e. the piece type which is either [" ", "K"], a regular piece
    # or a king.
    def swap(a,b):
        return (b,a) if a.strip() else (a,b) 

    for piece in pieces:
        row = piece["location"]["row"]
        col = piece["location"]["col"]
        loc = (row-1) * 8 + col-1
        if debug:
            print("(row,col) => ({},{}) => location on the board internally ({})".format(row,col,loc))

        # set the values that should appear on the board
        board[loc] = "{}-{}".format("{}{}".format(*swap(piece["type"],piece["color"])),
                                                   piece["owner"][0].upper())

    print("""
                {}
        +------+------+------+------+------+------+------+------+
      1 | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | 
        +------+------+------+------+------+------+------+------+
      2 | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} |
        +------+------+------+------+------+------+------+------+
      3 | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} |
        +------+------+------+------+------+------+------+------+
      4 | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} |
        +------+------+------+------+------+------+------+------+
      5 | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} |
        +------+------+------+------+------+------+------+------+
      6 | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} |
        +------+------+------+------+------+------+------+------+
      7 | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} |
        +------+------+------+------+------+------+------+------+
      8 | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} | {:4} |
        +------+------+------+------+------+------+------+------+
           1      2      3      4      5      6      7      8

        """.format(title,*board))


# initialize the pieces on the board pieces
pieces = []
human =  {}
computer = {}

debug = False  # check to see what the code is doing

# the template to create a piece is the same for both players
def create_piece(row,col,color,owner,ptype):
    return {"location":{"row":row,"col":col},
            "color":color,
            "owner":owner,
            "type":ptype}

# top of the display board
for row in range(1,4):
    for col in range(2 if (row % 2) else 1,9,2):
        if debug:
            print("Top: (row,col) => ({},{})".format(row,col))
        computer[(row,col)] = create_piece(row=row,col=col,color='W',owner='computer',ptype="")

# bottom of the display board
for row in [8,7,6]:
    for col in range(2 if (row % 2) else 1,9,2):
        if debug:
            print("Bottom: (row,col) => ({},{})".format(row,col))
        human[(row,col)] = create_piece(row=row,col=col,color='B',owner='human',ptype="")
       
#demonstrate removing a piece from the board
#pieces = [piece for piece in pieces if not (piece["location"]["row"] == 7 and piece["location"]["col"] == 2)]
pieces = [value for key,value in (list(human.items()) + list(computer.items())) ]

#show the board with all the pieces in their position
view(pieces=pieces,title="Test Board",debug=debug)


def move(player,old_row,old_col,new_row,new_col):  
    
    if (new_row,new_col) in player:
        print("ERROR: moving a piece to a location that is already occupied...... ({},{}) -> ({},{})".format(old_row,old_col,new_row,new_col)) 
        return player
    else:
        if player == human:
            if (new_row,new_col) == (old_row-1,old_col-1) or (new_row,new_col) == (old_row-1,old_col+1):
                player[(new_row,new_col)] = player[(old_row,old_col)]
                player[(new_row,new_col)]["location"]["row"] = new_row
                player[(new_row,new_col)]["location"]["col"] = new_col
                del player[(old_row,old_col)]
                return player 
            else:
                print("ERROR")
        elif player == computer:
            if (new_row,new_col) == (old_row+1,old_col-1) or (new_row,new_col) == (old_row+1,old_col+1):
                player[(new_row,new_col)] = player[(old_row,old_col)]
                player[(new_row,new_col)]["location"]["row"] = new_row
                player[(new_row,new_col)]["location"]["col"] = new_col
                del player[(old_row,old_col)]
                return player 
            else:
                print("ERROR")    
def askUserMove(player):
    game = True 
    while game:
        oldR = int(input("Old row: "))
        oldC = int(input("Old column: "))
        newR = int(input("Move to row:"))
        newC = int(input("Move to column: "))
    
        if newC<1 or newC>8 and newR<1 or newR>8:
            return("Out of bounds")
        
        else:
            move(player,oldR,oldC,newR, newC)
            game = False
        view(pieces=pieces,title="Human Move",debug=debug)

def computerMove(player):
    key_found = False
    move = []
    while key_found == False:
        #make a list of the pieces
        list_keys = list(player.keys())
        #choose a random piece
        piece = player[list_keys[random.randrange(0,len(list_keys))]]
        #new piece
        if (piece["location"]["row"]+1,piece["location"]["col"]+1) not in player:
            if piece["location"]["row"]+1 < 1 or piece["location"]["row"]+1 > 8 and piece["location"]["col"]+1 < 1 or piece["location"]["col"]+1 > 8:
                move.extend((piece["location"]["row"]+1,piece["location"]["col"]+1))

        elif (piece["location"]["row"]+1,piece["location"]["col"]-1) not in player:
            if piece["location"]["row"]+1 < 1 or piece["location"]["row"]+1 > 8 and piece["location"]["col"]-1 < 1 or piece["location"]["col"]-1 > 8:
                move.extend((piece["location"]["row"]+1,piece["location"]["col"]-1))
            
        elif len(move) == 0:
            key_found = False
        elif len(move) >= 1:
            key_found = True
    #choose the piece from the move
    print (piece["location"]["row"],piece["location"]["col"])
    print (piece["location"]["row"]+1)
    print(piece["location"]["row"])
    print (move)
    #if len(move) == 1:
        #move(player = computer, piece["location"]["row"],piece["location"]["col"],)
        #view(pieces=pieces,title="Computer Move",debug=debug)
    #else:
        
    
def main():
    game_over = False
    while game_over == False:
        askUserMove(player = human)
        computerMove(player = computer)
main ()