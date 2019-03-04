#BlackJack Class
#programming assignment 5
from graphics import *
from random import *
from playingcardclass import *
from deckclass import *
from buttonclass import *

class BlackJack:
    """Creates a BlackJack class"""

    def __init__(self, dHand = [], pHand = []):

        ###This initializes the two variables standing for the dealer's hand and player's hand
        self.dHand = dHand
        self.pHand = pHand

        #this creates a shuffled deck as variable within the class
        self.playingDeck = Deck()
        self.playingDeck.shuffledeck()

        

    def initDeal(self,gwin,xposD, yposD, xposP, yposP):
        
        #This creates the first and second card for the dealer and player 
        #it first uses the created dealcard method and then appends it into the empty lists
        self.firstcardD = self.playingDeck.dealCard()
        self.dHand.append(self.firstcardD)
        self.secondcardD = self.playingDeck.dealCard()
        self.dHand.append(self.secondcardD)

        self.firstcardP = self.playingDeck.dealCard()
        self.pHand.append(self.firstcardP)
        self.secondcardP = self.playingDeck.dealCard()
        self.pHand.append(self.secondcardP)

        #this gets the suit and rank from each card
        self.rank1D = self.dHand[0].getRank()
        self.suit1D = self.dHand[0].getSuit()
        self.rank2D = self.dHand[1].getRank()
        self.suit2D = self.dHand[1].getSuit()

        self.rank1P = self.pHand[0].getRank()
        self.suit1P = self.pHand[0].getSuit()
        self.rank2P = self.pHand[1].getRank()
        self.suit2P = self.pHand[1].getSuit()
        
        #this makes callable variables for the x and y positions 
        self.xposD, self.yposD = xposD, yposD
        self.xposP, self.yposP = xposP, yposP

        #Finally the two cards are created and drawn onto the given window
        dealer1 = Image(Point(self.xposD, self.yposD), "playingcards/" + self.suit1D + str(self.rank1D) + ".gif")
        dealer1.draw(gwin)
        dealer2 = Image(Point(self.xposD+100, self.yposD), "playingcards/" + self.suit2D + str(self.rank2D) + ".gif")
        dealer2.draw(gwin)

        player1 = Image(Point(self.xposP, self.yposP), "playingcards/" + self.suit1P + str(self.rank1P) + ".gif")
        player1.draw(gwin)
        player2 = Image(Point(self.xposP+100, self.yposP), "playingcards/" + self.suit2P + str(self.rank2P) + ".gif")
        player2.draw(gwin)

        #Creates face down red deck
        reddeckimg = Image(Point(630, 350), "playingcards/b2fv.gif")
        reddeckimg.draw(gwin)
        #creates face down blue deck
        bluedeckimg = Image(Point(720,350), "playingcards/b1fv.gif")
        bluedeckimg.draw(gwin)
        
    def hit(self,gwin,xPos,yPos):
        #uses dealCard method from the deck class and appends the list of the total cards that the player has
        self.newcardP = self.playingDeck.dealCard()
        self.pHand.append(self.newcardP)

        #does for loop for the number of cards the player has
        for i in range(len(self.pHand)):
            self.newrankP = self.pHand[i].getRank()#indexes the new card's rank
            self.newsuitP = self.pHand[i].getSuit()#indexes the new card's suit
            #presents the image of the card
            newplayercard = Image(Point(xPos, yPos), "playingcards/" + self.newsuitP + str(self.newrankP) + ".gif")
            newplayercard.draw(gwin)
            

    def evaluateHand(self, hand):
        #sets the total equal to 0 
        total =  0
        hasAce = False#initalizes the hasAce statement

        for card in hand:          #for loop for every card in either the dealer or the player's hand 
            total = card.BJValue()+total#creates new total value depending on the card and its value in Blackjack
            if  card.getRank()== 1:#also changes the hasAce to True if an ace appears 
                hasAce = True
            
            
        if hasAce and total+10 <= 21:#adds condition that if the total + 10 is less than 21 and hasAce is true than add 10 to the total 
            
                total = total + 10
        return total           
        
    def dealerPlays(self,gwin,xPos,yPos):
         
       #Creates new dealer card using dealCard method from the deack class
        self.newcardD = self.playingDeck.dealCard()
        self.dHand.append(self.newcardD)#appends it to the dealer's hand

        self.newrankD = self.dHand[len(self.dHand)-1].getRank()#gets the suit
        self.newsuitD = self.dHand[len(self.dHand)-1].getSuit()#gets the rank
        newdealercard = Image(Point(xPos, yPos), "playingcards/" + self.newsuitD + str(self.newrankD) + ".gif")#creates image representing card image
        newdealercard.draw(gwin)
            
         
         
         
def main():
    #Creates Graphics window, sets background to green, and uses initDeal method
    win = GraphWin("BlackJack", 800,700)
    win.setBackground("dark green")
    b = BlackJack()
    b.initDeal(win,200,200,200,550)
    introtext = Text(Point(400,50), "Welcome to BlackJack click Hit or Stand to begin.")#introduction text
    introtext.draw(win)

    #Text presenting the dealer's hand and total value
    dealertext = Text(Point(200,130), "Dealer Hand:")
    dealertext.draw(win)
    dealertotal = Text(Point(200, 270), "Dealer Total:")
    dealertotal.draw(win)
    dealerhand = Text(Point(260,270), str(b.evaluateHand(b.dHand)))
    dealerhand.draw(win)

    #text presenting the player's hand and total card value
    playertext = Text(Point(200, 480), "Player Hand:")
    playertext.draw(win)
    playertotal = Text(Point(200, 620), "Player Total:")
    playertotal.draw(win)
    playerhand = Text(Point(260,620), str(b.evaluateHand(b.pHand)))
    playerhand.draw(win)
    
    #creates three buttons. Hit, Stand, Exit
    Hitb = Button(win, Point(350,350), 110, 75, "Hit")
    Standb = Button(win,Point(500,350), 110, 75, "Stand")
    Exitb = Button(win, Point(400, 650), 100, 50 , "Exit")

    #Creates the text whenever a game is over
    endtext = Text(Point(400,440), "Click anywhere to close")
    endtext.setStyle("bold italic")
    endtext.setSize(15)

    #creates text whenever dealer wins
    Dealerwin = Text(Point(400,415), "The Dealer has won!")
    Dealerwin.setStyle("bold italic")
    Dealerwin.setSize(15)

    #takes inital mouseclick and initializes hitcounter
    pt = win.getMouse()
    hitcounter = 0
    
    while not Exitb.clicked(pt):#Creating while loop for when anything but the exit but is clicked
        
        if Hitb.clicked(pt):
            
            hitcounter = hitcounter + 10 #this increases the value of the hitcounter by 10 everytime the hit button is clicked
            b.hit(win,300+8*hitcounter,550)#uses hit method
            playerhand.setText(str(b.evaluateHand(b.pHand)))#sets the total text to the new value
            
            #if loop for if the player total is greater than 21
            if b.evaluateHand(b.pHand) > 21:
                #Dealer win text
                Dealerwin = Text(Point(400,415), "You Busted! The Dealer has won!")
                Dealerwin.setStyle("bold italic")
                Dealerwin.setSize(15)
                Dealerwin.draw(win)
                
                #end text drawn
                endtext.draw(win)

                #mouseclick and then the window closes
                win.getMouse()
                win.close()            


        if Standb.clicked(pt):#if loop for stand button
            
            #This says that if its clicked and the dealer's hand is greater than or equal to the player's than the dealer wins
            if b.evaluateHand(b.dHand)>b.evaluateHand(b.pHand) or b.evaluateHand(b.dHand)==b.evaluateHand(b.pHand):
                Dealerwin.draw(win)
                endtext.draw(win)
                win.getMouse()
                win.close()
            #this elif is if the player hand is greater than the dealer hand 
            elif b.evaluateHand(b.dHand)<b.evaluateHand(b.pHand):
                
                dealercount = 0#creates dealercount variable equal to 0 which helps space out the card
                #While loop so the dealerplays method will continue until the dealer's hand is greater than 17 and greater than the player's hand
                while b.evaluateHand(b.dHand)<17 and b.evaluateHand(b.dHand)<b.evaluateHand(b.pHand):
                    dealercount = dealercount + 1
                    b.dealerPlays(win, 300+(100*dealercount), 200)
                    dealerhand.setText(str(b.evaluateHand(b.dHand)))
                
                #however if the dealer's hand is greater than 21 than the dealer would bust           
                if b.evaluateHand(b.dHand)>21:
                    Dealerbust = Text(Point(400,415), "The Dealer has busted! You Won!")
                    Dealerbust.setStyle("bold italic")
                    Dealerbust.setSize(15)
                    Dealerbust.draw(win)
                    endtext.draw(win)
                    win.getMouse()
                    win.close()

                #same as the inital if statement from the beginning of the stand button if statement
                elif b.evaluateHand(b.dHand)>b.evaluateHand(b.pHand) or b.evaluateHand(b.dHand)==b.evaluateHand(b.pHand):
                    Dealerwin.draw(win)
                    endtext.draw(win)
                    win.getMouse()
                    win.close()
                    
                #Lastly if the player's hand is still greater than the dealer's hand then the player has won
                elif b.evaluateHand(b.dHand)<b.evaluateHand(b.pHand):
                    Playerwin = Text(Point(400,415), "You won!")
                    Playerwin.setStyle("bold italic")
                    Playerwin.setSize(15)
                    Playerwin.draw(win)
                    endtext.draw(win)
                    win.getMouse()
                    win.close()
        pt = win.getMouse() # gets moust click that way the game has no stops  
            
    win.close()#if exit button is clicked than the window must close
main()
        
        
        
    
        
