#War 2.0
#Tyler Brown

import random	
def playRound(playerA, playerB):
	cardA = playerA.pop()
	cardB = playerB.pop()
	rankA = getRank(cardA)
	rankB = getRank(cardB)
	if (rankA > rankB):
		playerA.insert(0, cardA)
	elif (rankB > rankA):
		playerB.insert(0, cardB)
	else:
		WAR(playerA, playerB)
	return playerA, playerB

def WAR(playerA, playerB):
	# See the README.md file for instructions on coding 
	# This module.
	return playerA, playerB

def getRank(anyCard):
	return anyCard % 13

def main():
	deck = []
	playerAHand = []
	playerBHand = []
	gameCounter = 0
	cardA = 0
	cardB = 0
	rankA = 0
	rankB = 0
	# Create deck
	for deckIndex in range(52):
		deck.append(deckIndex)
	# Shuffle
	random.shuffle(deck)
	# Deal half
	for x in range(26):
		playerAHand.append(deck.pop())
		playerBHand.append(deck.pop())
	while len(playerAHand) > 0 and len(playerBHand) > 0:
		gameCounter += 1
		playerAHand, playerBHand = playRound(playerAHand, playerBHand)
	print "There were" , gameCounter , "rounds played."

if __name__ == '__main__':
	main()
