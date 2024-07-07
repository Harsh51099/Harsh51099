import random
moves = ["rock","paper","scissors"]
keep_playing ="true"

while (keep_playing == "true"):
    cmove = random.choice (moves)
    pmove = input ("What is your move? rock,paper or scissors?")

    print ("The computer chose",cmove)
    if(cmove == pmove):
          print("Tie")
    elif(pmove =="rock" and cmove == "scissors"):
          print("player won")
    elif(pmove =="rock" and cmove == "paper"):
          print("computer won")
    elif(pmove =="paper" and cmove == "rock"):
          print("player won")
    elif(pmove =="paper" and cmove == "scissors"):
          print("computer won")
    elif(pmove =="scissors" and cmove == "paper"):
          print("player won")
    elif(pmove =="scissors" and cmove == "rock"):
          print("computer won")
