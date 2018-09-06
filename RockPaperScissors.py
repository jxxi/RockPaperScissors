from random import randint

computer =	{
    1 : "rock",
    2 : "paper",
    3 : "scissors"
}

player =	{
    "r" : "rock",
    "p" : "paper",
    "s" : "scissors"
}

playerInput = input('rock (r), paper (p), or scissors (s)?')
playerChoice = ""

if player.has_key(playerInput):
  playerChoice = player[playerInput]
else:
  print("Invalid choice")
  
  
computerInput = randint(1,3)
computerChoice = computer[computerInput]

print(playerChoice + ' vs ' + computerChoice)

if playerChoice == computerChoice:
  print('Draw!')
  
elif playerChoice == "rock" and computerChoice == 'paper':
  print('Computer wins!')

elif playerChoice == "rock" and computerChoice == 'scissors':
  print('Player wins!')

elif playerChoice == "paper" and computerChoice == 'rock':
  print('Player wins!')

elif playerChoice == "paper" and computerChoice == 'scissors':
  print('Computer wins!')
  
elif playerChoice == "scissors" and computerChoice == 'paper':
  print('Player wins!')

elif playerChoice == "scissors" and computerChoice == 'rock':
  print('Computer wins!')