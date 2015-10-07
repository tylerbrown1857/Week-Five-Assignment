#Programming the Game of War#  

##Version 1##
This version of War has a poetic similarity to war in real life; no one wins in war. 
If both players play a card of the same value (ranging from low to high, 2-Ace), 
both players remove that card from play.  

You will discover that even with this reduction in the card count,
the gameplay will run for a long time. I mean a LONG time.
You may find that you will want to pause the gameplay after a certain number of 
rounds (10,000. I kid you not).  To pause, simply throw in an *input* statement.
You don't have to do anything with the input, it will just pause the run.

##Version 2##
In order to save time, you can implement this rule.
Any card that loses a battle is dead, or eliminated from the game. 
The card that wins returns to the original owner. This will result in a average
of about 45 rounds per run.

##Version 3##
In the final version, implement the full function of the WAR method for
ONE round. I.E.  
    1. Save off 3 cards from each player.    
    2. Match the 4th card.  
    3. Winner gets ALL the cards.   
    4. If this play is a tie, all cards are discarded (lost).  