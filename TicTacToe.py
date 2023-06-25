board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]


def team_selection():
    # Lets the user select whether Team 'x' or Team 'o' will go first.
    start_team = input(f'Please select which team is going first: ')
    while True:
        if start_team == 'x' or start_team == 'o':
            return start_team
        else:
            start_team = input(f'Please select either Team \'x\' or Team \'o\': ')


def print_board():
    # Prints out the TicTacToe board for the user to see.
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')


def update_board(team):
    # Updates the board with the users input every turn.
    while True:
        square = int(input(f'Team {team} please select an open square: '))
        square -= 1
        if board[square] == square+1:
            board[square] = team
            break


def check_win():
    # Checks horizontal wins
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:
        return True
    # Checks vertical wins
    elif board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        return True
    # Checks diagonal wins
    elif board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True
    # If no wins have occurred then game continues.
    else:
        return False


def check_tie():
    # Checks to see if all squares are filled, if not game continues.
    for i in board:
        if i != 'x' and i != 'o':
            return False
    # If all squares are filled and a win has not been determined yet, then the game is determined a tie.
    return True


def change_team(team):
    # Changes team playing at the end of every turn.
    if team != 'o':
        return 'o'
    else:
        return 'x'


def main():
    team = team_selection()
    print_board()
    # Loops through a turn sequence until either a win or tie is determined.
    while True:
        update_board(team)
        print_board()
        # If a win has occurred the game ends.
        if check_win():
            print(f'Team {team} has won! Congratulations!')
            break
        # If a tie has occurred the game ends.
        elif check_tie():
            print(f'This game is a tie! Good try!')
            break
        # If neither a win or a tie has occurred the team changes and the next turn commences.
        else:
            team = change_team(team)


if __name__ == '__main__':
    main()
