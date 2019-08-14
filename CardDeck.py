#This program will create a deck of cards and shuffle them
import random

cardfaces =[]
suits = ["♥", "♦", "♣", "♠"] #got the characters from word ;-)
royals = ["J", "Q", "K", "A" ]
deck =[]

for i in range(2,11):
    cardfaces.append(str(i))

for j in range(4):
    cardfaces.append(royals[j])

for k in range(4):
    for l in range(13):
        card = (cardfaces[l] +" "+ suits[k])
        deck.append(card)

random.shuffle(deck)

for m in range (52):
    print ("[ " + deck[m] + " ]")
   




