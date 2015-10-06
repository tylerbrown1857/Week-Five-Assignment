#!/usr/bin/env python
# encoding: utf-8
"""
GameOfWar.py

Created by Neumann, Daniel on 2015-10-06.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.
"""

import random

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
	for x in range(26)
	PlayerAHand.append(Deck.pop())
	PlayerBHand.append(Deck.pop())
	
	if len(Deck) != 0:
		print("There is a problem: Deck = " ,len(deck))
		break
	
	# Main Gameplay
		
	while (len(PlayerAHand) > 0 AND len(PlayerBHand) > 0):
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	
		




def playHand(PlayerA, PlayerB):
	
	
	return PlayerA, PlayerB


def War(PlayerA, PlayerB):
	
	return PlayerA, PlayerB
	










if __name__ == '__main__':
	main()

