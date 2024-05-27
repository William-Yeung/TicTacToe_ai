
grid = [[0,0,0],
        [0,0,0],
        [0,0,0]]
openSpots = 9

def bestMove():
    best = float('-inf')
    move1 = 0
    move2 = 0
    for i in range (3):
        for j in range (3):
            if grid[i][j] == 0:
                grid[i][j] = 2
                score = minimax(0, False)
                grid[i][j] = 0
                if(score > best):
                    best = score
                    move1 = i
                    move2 = j
    grid[move1][move2] = 2


def minimax(depth, isMax):
    result = winner()
    score = 0
    if result != 0:
        if result == 1:
            score = -1
        if result == 2:
            score = 1
        if result == 3:
            score = 0
        return score
    if isMax:
        best = float('-inf')
        for i in range (3):
            for j in range (3):
                if grid[i][j] == 0:
                    grid[i][j] = 2
                    score = minimax(depth+1, False)
                    grid[i][j] = 0
                    best = max(score, best)
        return best
    else:
        best = float('inf')
        for i in range (3):
            for j in range (3):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    score = minimax(depth+1, True)
                    grid[i][j] = 0
                    best = min(score, best)
        return best
                    

def vert_win():
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] == 1:
                return 1
            elif grid[i][0] == 2:
                return 2
    return 0

def hor_win():
    for i in range (3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            if grid[i][0] == 1:
                return 1
            elif grid[i][0] == 2:
                return 2
    return 0


def diag_win():
    if grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[1][1] == 1:
            return 1
        elif grid[1][1] == 2:
            return 2
    if grid[0][2] == grid[1][1] == grid[2][0]:
        if grid[1][1] == 1:
            return 1
        elif grid[1][1] == 2:
            return 2
    return 0

def winner():
    if vert_win() != 0:
        #print("Winner player " + str(vert_win()))
        return vert_win()
    if hor_win() != 0:
        #print("Winner player " + str(hor_win()))
        return hor_win()
    if diag_win() != 0:
        #print("Winner player " + str(diag_win()))
        return diag_win()
    if openSpots == 0:
        #print("Tie")
        return 3
    return 0

def print_grid():
    for i in range(3):
        temp = ""
        for j in range(3):
            if grid[i][j] == 0:
                temp = temp + " _ "
            elif grid[i][j] == 1:
                temp = temp + " O "
            elif grid[i][j] ==  2:
                temp = temp + " X "
        print(temp)

def reset_grid():
    for i in range(3):
        for j in range(3):
            grid[i][j] = 0

def set_move(player, action):
    if action == 1:
        grid[0][0] = player
    elif action == 2:
        grid[0][1] = player
    elif action == 3:
        grid[0][2] = player
    elif action == 4:
        grid[1][0] = player
    elif action == 5:
        grid[1][1] = player
    elif action == 6:
        grid[1][2] = player
    elif action == 7:
        grid[2][0] = player    
    elif action == 8:
        grid[2][1] = player
    elif action == 9:
        grid[2][2] = player

turn = 2 ##1 for player, 2 for opponent

while(turn != 0):
    print_grid()
    print()
    if turn == 1:
        move = int(input("Enter Move:"))
        set_move(turn, move)
        turn = 2
    elif turn == 2:
        bestMove()
        turn = 1
    openSpots = openSpots - 1
    if winner() != 0:
        break

print_grid()
if(winner() == 1):
    print("Player Wins!")
elif(winner() == 2):
    print("AI Wins")
else:
    print("Tie")