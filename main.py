import random


def start_game():
    hands = ['R', 'P', 'S']
    loop_hole = 0

    print('Starting the Rock Paper Scissors game!')
    player_name = input('Please enter your name: ')

    while loop_hole == 0:
        print('Pick a hand: (R for Rock, P for Paper, S for Scissors)')
        player_hand = input('Please enter a hand: ')
        player_hand.upper()

        for x in player_hand:
            if player_hand == 'R' or 'P' or 'S':

                cpu_hand = random.choice(hands)

                print(player_name.capitalize() + '(' + player_hand.upper() + ')' + " : " "CPU" + '(' + cpu_hand + ')')

                if player_hand == 'R' and cpu_hand == 'S':
                    print("Congratulations, You Won")
                    loop_hole += 1

                elif player_hand == 'S' and cpu_hand == 'P':
                    print("Congratulations, You Won")
                    loop_hole += 1

                elif player_hand == 'P' and cpu_hand == 'R':
                    print("Congratulations, You Won")
                    loop_hole += 1

                elif player_hand == cpu_hand:
                    print("It's a tie")

                else:
                    print("You lose")
                    loop_hole += 1

            else:
                print("Please enter a valid hand, try again")



start_game()
