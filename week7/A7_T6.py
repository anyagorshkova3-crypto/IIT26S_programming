import random
random.seed(1234)
OPTIONS = ("rock", "paper", "scissors")
ART = (
      r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
)
def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    name = input("Insert player name: ")
    player_wins = 0
    bot_wins = 0
    draws = 0
    print(f'Welcome {name}!')
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")
    player_choice = ""
    while player_choice != "0":
        print("Options:\n1 - Rock\n2 - Paper\n3 - Scissors\n0 - Quit game")
        player_choice = input("Your choice: ")
        if player_choice != "0":
            print("Rock! Paper! Scissors! Shoot!\n")
            print("#" * 25)
            print(f"{name} chose {OPTIONS[int(player_choice) - 1]}.")
            print(ART[int(player_choice) - 1])
            print("#" * 25)
            bot_choice = random.randint(1, 3)
            print(f"RPS-3PO chose {OPTIONS[bot_choice - 1]}.")
            print(ART[bot_choice - 1])
            print("#" * 25)
            print()
            if int(player_choice) == bot_choice:
                print(f"Draw! Both players chose {OPTIONS[bot_choice - 1]}.")
                draws += 1
                print()
            elif int(player_choice) == 1 and bot_choice == 3:
                print(f"{name} {OPTIONS[int(player_choice) - 1]} beats RPS-3PO {OPTIONS[bot_choice - 1]}.")
                player_wins += 1
                print()
            elif int(player_choice) == 2 and bot_choice == 1:
                    print(f"{name} {OPTIONS[int(player_choice) - 1]} beats RPS-3PO {OPTIONS[bot_choice - 1]}.")
                    player_wins += 1
                    print()
            elif int(player_choice) == 3 and bot_choice == 2:
                    print(f"{name} {OPTIONS[int(player_choice) - 1]} beats RPS-3PO {OPTIONS[bot_choice - 1]}.")
                    player_wins += 1
                    print()
            elif int(player_choice) == 1 and bot_choice == 2:
                    print(f"RPS-3PO {OPTIONS[bot_choice - 1]} beats {name} {OPTIONS[int(player_choice) - 1]}.")
                    bot_wins += 1
                    print()
            elif int(player_choice) == 2 and bot_choice == 3:
                    print(f"RPS-3PO {OPTIONS[bot_choice - 1]} beats {name} {OPTIONS[int(player_choice) - 1]}.")
                    bot_wins += 1
                    print()
            elif int(player_choice) == 3 and bot_choice == 1:
                    print(f"RPS-3PO {OPTIONS[bot_choice - 1]} beats {name} {OPTIONS[int(player_choice) - 1]}.") 
                    bot_wins += 1    
                    print()  
    print()
    print("Results:")  
    print(f"{name} - wins ({player_wins}), losses ({bot_wins}), draws ({draws})")
    print(f"RPS-3PO - wins ({bot_wins}), losses ({player_wins}), draws ({draws})") 
    print()            
    print("Program ending.")
main()