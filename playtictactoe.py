
from itertools import combinations

grid_list = [2, 6, 7,
             10, 5, 0,
             3, 4, 8]

grid_dict = {
    '1':2,
    '2':6,
    '3':7,
    '4':10,
    '5':5,
    '6':0,
    '7':3,
    '8':4,
    '9':8
    }

char_map = {
    0: "X",
    1: "0"
    }


def print_grid():
    print()
    for i in range(len(map_list)):
        new_str = ''.join(map_list[i])
        print(new_str)

    print()
                          
while True:

    map_list = [['-',' ','|','|',' ','-',' ','|','|',' ','-'],
                ['='] * 11,
                ['-',' ','|','|',' ','-',' ','|','|',' ','-'],
                ['='] * 11,
                ['-',' ','|','|',' ','-',' ','|','|',' ','-']]

    player1_list = []
    player2_list = []

    used_moves = []

    move_count = 0

    current_player = 0

    game_over = False

    while game_over == False:

        print_grid()

        print(f"Player {str(current_player % 2 + 1)}, where would you like to move?")
        player_input = input("Please enter a number 1-9, as they would appear on a phone unlock screen.\n\n> ")

        while True:
            if player_input not in grid_dict:
                player_input = input("\nTry again. Enter a number 1-9\n\n> ")
            elif player_input not in used_moves:

                if current_player % 2 == 0:
                    player1_list.append(grid_dict[player_input])
                else:
                    player2_list.append(grid_dict[player_input])
                    
                used_moves.append(player_input)
                
                if int(player_input) <= 3:
                    char_loc = 5 * ((int(player_input) + 2) % 3)
                    map_list[0][char_loc] = char_map[current_player%2]
                    
                elif int(player_input) <= 6:
                    char_loc = 5 * ((int(player_input) + 2) % 3)
                    map_list[2][char_loc] = char_map[current_player%2]

                else:
                    char_loc = 5 * ((int(player_input) + 2) % 3)
                    map_list[4][char_loc] = char_map[current_player%2]
                    
                current_player += 1
                break
            else:
                player_input = input("\nThis move has already been played. Enter a different number 1-9\n\n> ")

        move_count += 1

        if move_count >= 5:

            player1combs = combinations(player1_list, 3)

            while True:
                for combination in list(player1combs):
                    check = 0

                    for i in range(len(combination)):
                        check += combination[i]

                    if check == 15:
                        print_grid()
                        print('=' * 20)
                        print("\nPlayer 1 wins!!\nNice work!\n")
                        print('=' * 20)
                        game_over = True
                        break
                    
                break

        if move_count >= 6:

            player2combs = combinations(player2_list, 3)

            while True:
                for combination in list(player2combs):
                    check = 0

                    for i in range(len(combination)):
                        check += combination[i]

                    if check == 15:
                        print_grid()
                        print('=' * 20)
                        print("\nPlayer 2 wins!!\nNice work!\n")
                        print('=' * 20)
                        game_over = True
                        break
                
                break

        if move_count == 9 and game_over == False:
            print("\nThe game is drawn. Tough battle!")
            game_over = True


    useless = input("\nPress enter to play again")








