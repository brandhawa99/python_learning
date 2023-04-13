# RPS Game
# Author: Baltej Randhawa

import random


def get_choice():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return {"player": player_choice, "comp": computer_choice}


def check_win(player, computer):
    if player == computer:
        print(f"TIE: You Both chose {player}")
        return
    if (
        player == "rock"
        and computer == "scissors"
        or player == "paper"
        and computer == "rock"
        or player == "scissors"
        and computer == "paper"
    ):
        print(f"YOU WIN: You chose {player} computer chose {computer}")
        return
    else:
        print(f"YOU LOSE: You chose {player} computer chose {computer}")
        return


def main():
    i = 0
    for i in range(5):
        choices = get_choice()
        check_win(choices["player"], choices["comp"])


main()
