'''Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them,
 return out a message of congratulations to the winner, 
 and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

import sys

player1 = input("Player1 do yo want to choose rock, paper or scissors?")
player2 = input("Player2 do you want to choose rock, paper or scissors?")

def compare(p1,p2):
	
	if p1 == p2:
		return("It's a tie")
	elif p1=="rock":
		if p2=="paper":
			return("Player2 wins")
		else:
			return("Player1 wins")
	elif p1=="paper":
		if p2=="rock":
			return("Playler1 wins")
		else:
			return("Player2 wins")
	elif p1=="scissors":
		if p2=="rock":
			return("Player2 wins")
		else:
			return("Player1 wins")
	else:
		return("invalid input")
		sys.exit()
		
print(compare(player1,player2))
