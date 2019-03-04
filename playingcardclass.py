#Playing Card class
from graphics import *
from random import *
class PlayingCard:

    """Creates playing card with methods to figure out the suit, rank, and
    blackjack value"""

    def __init__(self,Rank,Suit):

        """creates card example: card = PlayingCard(3,d)"""
        self.rank = Rank - 1 #rank - 1 so that, for example, when rank = 1, program doesnt give second card in list
        self.suit = Suit
        #created variable for each suit
        self.allranks = [ "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.allsuits = {"s": "spades", "d": "diamonds","c": "clubs", "h": "hearts"}


            
    def getRank(self):
        """returns the rank of the card"""
        return self.rank + 1 
    
    def getSuit(self):
        """returns the suit of the card"""
        return self.suit

    
    def __str__(self):
        """returns a string that names the card. For example ace of spades"""
        return self.allranks[self.rank] + ' of ' + self.allsuits[self.getSuit()] 

    def BJValue(self):
        """returns value of card according to the rules of black jack"""
        
        if self.getRank() > 10: #all cards with rank greater than 10 have a value of 10
            
            return 10
        else:
            
            return self.rank + 1

def main():
    #quick test for the class
    c = PlayingCard(11,"h")
    
    print(c)
    print(c.BJValue())
    print(c.getRank())
    


    
if __name__ == '__main__':
    main()


        
