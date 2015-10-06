#!/usr/bin/env python
# encoding: utf-8
"""
GameOfWar.py

Created by Neumann, Daniel on 2015-10-06.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.
"""

import random	
WARCounter = 0

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	
	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	if len(Deck) != 0:
		print("There is a problem: Deck = " ,len(Deck))
		exit()
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		print("Game counter = " + str(gameCounter))
		print("A hand:" + str(PlayerAHand))
		print("B hand:" + str(PlayerBHand))
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
	#	if gameCounter > 10:
	#		exit()
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	
		




def playRound(PlayerA, PlayerB):
	
	print("Playing a round. Starting Counts")
	print("Player A has ", str(len(PlayerA)), " Player B has ", str(len(PlayerB)))

	ACard = PlayerA.pop()
	BCard = PlayerB.pop()
	
	print("Cards popped, should be 1 less")		
	print("Player A has ", str(len(PlayerA)), " Player B has ", str(len(PlayerB)))

	# Call function to display the card's Rank
	A_rank = getRank(ACard)
	B_rank = getRank(BCard)
	
	print ("Player A plays " + str(A_rank))
	print ("Player B plays " + str(B_rank))
	
	# Compare ranks
	
	if A_rank > B_rank:
		print("Player A wins\n")
		PlayerA.insert(0,ACard)
		PlayerA.insert(0,BCard)
	elif A_rank < B_rank:
		print("Player B wins\n")
		PlayerB.insert(0,ACard)
		PlayerB.insert(0,BCard)
	else:
		#WAR!!
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
	
	print("End of round")
	print("Player A has ", str(len(PlayerA)), " Player B has ", str(len(PlayerB)))
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	# for now if there is a war, both players lose a card.
	print("Everyone loses in a War")
	X = input("War")
	return PlayerA, PlayerB


	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()

