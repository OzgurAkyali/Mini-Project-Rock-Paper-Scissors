score_user = 0
score_pc = 0

import random

print("---ROCK.PAPER.SCISSORS.GAME---")
print("Rock(0), Paper(1), Scissors(2)")
print("First to reach 3 wins")

while score_user < 3 and score_pc < 3:
    player = int(input("Make your choice: "))
    computer = random.randint(0, 2)
    if player == computer:
        print("It's a tie")
    elif player < computer:
        score_pc += 1
        print("Computer wins this round \nPlayer:", score_user, "Computer:", score_pc)
    else:
        score_user += 1
        print("Player wins this round \nPlayer:", score_user, "Computer:", score_pc)

print("------Game Over------")
print("Final Score -> Player:", score_user, "Computer:", score_pc)