import random

choices=["Snake","Water","Gun"]

# Game Loop
computer_score=0
player_score=0


print("Welcome to Snake,Water and Gun Game")
print("rules: Snake Beats Water, Water Beats Gun, Gun Beats Snake")  

while True:
    player_choice=input("Enter your choice: (Snake/Water/Gun)")
    if player_choice=="Quit":
        break

    if player_choice not in choices:
        print("Invalid Choices")
        continue

    computer_choice=random.choice(choices)
    print(f"Computer Chose: {computer_choice}")

    if player_choice==computer_choice:
        print("Tie!!")
    elif (player_choice == "snake" and computer_choice == "water") or \
         (player_choice == "water" and computer_choice == "gun") or \
         (player_choice == "gun" and computer_choice == "snake"):
        player_score += 1
        print("You win this round!")
    else:
        computer_score += 1
        print("Computer wins this round!")
    
    print(f"Score → You: {player_score} | Computer: {computer_score}\n")
    
    if player_score == 5:
        print("🎉 YOU WIN THE GAME! 🎉")
        break
    if computer_score == 5:
        print("Computer wins the game! Better luck next time.")
        break
