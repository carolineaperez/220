"""
Name: Caroline Perez
lab10.py
"""

def build_board():
    tictactoe_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return tictactoe_list

def display_board(tictactoe_list):
    counter = 0
    print("----------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(tictactoe_list[counter], end="|")
            counter += 1
        print()
    print("----------")

def place_spot(tictactoe_list, spot, marker):
    tictactoe_list[spot-1] = marker

def legal_spot(tictactoe_list, spot):
    if ((tictactoe_list[spot-1] == 'X' or tictactoe_list[spot-1] == "0") or (spot < 1 or spot > 9)):
        return False
    else:
        return True

def game_won(tictactoe_list):
    wincon = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7]]
    for condition in wincon:
        counter = 0
        for spot in condition:
            if tictactoe_list[spot-1] == 'X':
                counter += 1
            if counter == 3:
                return "X Wins"
    for condition in wincon:
        counter = 0
        for spot in condition:
            if tictactoe_list[spot-1] == 'Y':
                counter += 1
            if counter == 3:
                return "Y Wins"

def game_over(tictactoe_list, turnCount):
    if ((game_won(tictactoe_list) == "X wins" or game_won(tictactoe_list) == "Y Wins" )
            or (turnCount >9)):
        return True
    else:
        return False

def play_Game():
    tictactoe_list = build_board()
    turnCount = 1
    while not game_over(tictactoe_list, turnCount):
        display_board(tictactoe_list)
        if turnCount % 2 == 0:
            print('It is X turn')
            spot = eval(input("enter the spot where you want to place X "))
            if legal_spot(tictactoe_list, spot):
                place_spot(tictactoe_list, spot, "X")
            if game_over(tictactoe_list, turnCount):
                if game_won(tictactoe_list):
                    display_board(tictactoe_list)
                    print(" X Wins")

        if turnCount % 2 == 1:
            print('It is Y turn')
            spot = eval(input("enter the spot where you want to play Y "))
            if legal_spot(tictactoe_list, spot):
                place_spot(tictactoe_list, spot, "Y")
            if game_over(tictactoe_list, turnCount):
                if game_won(tictactoe_list):
                    display_board(tictactoe_list)
                    print(" Y Wins")

        turnCount += 1




def main():
    # add other function calls here
    play_Game()
    pass


main()
