#War 3.0
#Tyler Brown

import random	
def playRound(playerA, playerb):
	#takes a card from each player
	cardA = playerA.pop()
	cardB = playerb.pop()
	#gets the rank of each card
	rankA = getRank(cardA)
	rankB = getRank(cardB)
	#check winner
	if rankA > rankB:
		playerA.insert(0, cardA)
		playerA.insert(0, cardB)
	elif rankB > rankA:
		playerb.insert(0, cardB)
		playerb.insert(0, cardA)
	else:
		#check war conditions
		if len(playerA) < 4:
			playerA = []
			print("Player B wins!")
		elif len(playerb) < 4:
			playerb = []
			print("Player A wins!")
		else:
			playerA, playerb = WAR(playerA, playerb)
	return playerA, playerb
	
def WAR(playerA, playerb):
	savedCardsA = []
	savedCardsB = []
	warCardA = 0
	warCardB = 0
	rankWarA = 0
	rankWarB = 0
	#save top three cards
	for i in range(0,3):
		savedCardsA.append(playerA.pop())
		savedCardsB.append(playerb.pop())
		#takes card for war
		warCardA = playerA.pop()
		warCardB = playerb.pop()
		#gets rank
		rankWarA = getRank(warCardA)
		rankWarB = getRank(warCardB)
		#check winner
		if rankWarA > rankWarB:
			playerA.insert(0, warCardA)
			playerA.insert(0, warCardB)
			playerA = savedCardsA + playerA
			playerA = savedCardsB + playerA
		elif rankWarB > rankWarA:
			playerb.insert(0, warCardB)
			playerb.insert(0, warCardA)
			playerb = savedCardsB + playerb
			playerb = savedCardsA + playerb
	else:
		print("This WAR is over.")
		return playerA, playerb

def getRank(anyCard):
	return anyCard % 13

def main():
	Deck = []
	playerAHand = []
	playerbHand = []
	gameCounter = 0
	cardA = 0
	cardB = 0
	rankA = 0
	rankB = 0
	# Create deck
	for i in range(52):
		Deck.append(i)
	# Shuffle
	random.shuffle(Deck)
	# Deal half
	for x in range(26):
		playerAHand.append(Deck.pop())
		playerbHand.append(Deck.pop())
	while len(playerAHand) > 0 and len(playerbHand) > 0:
		gameCounter += 1
		playerAHand, playerbHand = playRound(playerAHand, playerbHand)
	print "There were ", gameCounter, " rounds played"

if __name__ == '__main__':
	main()
