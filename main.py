import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rps_list = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
player_select = rps_list[player]
bot = random.randint(0, 2)
bot_select = rps_list[bot]

#0rock - 1paper - 2scissors
who_win = 0
if player_select == 0 and bot_select == 2:
  who_win = "You Win"
elif player_select == 1 and bot_select == 0:
  who_win = "You Win"
elif player_select == 2 and bot_select == 1:
  who_win = "You Win"
elif player_select == bot_select:
  who_win = "Draw"
else:
  who_win = "You Lose"

print(f"{player_select}\nComputer Chose:\n{bot_select}\n{who_win}")