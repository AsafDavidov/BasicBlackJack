##Deck Class
#Asaf Davidov
from random import *
from playingcardclass import *
class Deck:
    """Creates class that represents a deck of cards"""

    def __init__(self, Deck = []):  #creates deck
        self.fulldeck = Deck
        for s in ["d", "c", "h", "s"]:
            for r in range(1,14): #goes through all 13 cards in each suite
                self.fulldeck.append(PlayingCard(r,s))

        
    def shuffledeck(self):
        """Creates a shuffled deck"""
        shuffle(self.fulldeck)


    def dealCard(self):
        """Returns a single card from the top of the deck and removes the card"""
        dealtcard = self.fulldeck.pop()
        return dealtcard

    def cardsLeft(self):
        """Returns the number of cards remaining in the deck"""
        return len(self.fulldeck)

    def printDeck(self): #prints deck
        print(self.fulldeck)


def main():
    #creates quick test for the deck class
    d = Deck()
    d.shuffledeck() #shuffle deck randomly
    print(d.fulldeck)


if __name__ == '__main__':
    main()
