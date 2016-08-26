"""
This encapsulates the game: take a dictionary, a bunch of anagrams, and a bag of tiles, and start playing
"""

import Player,Rack,Tiles,Anagrams,Dictionary

class Game():
    def __init__(self,lexicon,anagrams,bag):
        self.lexicon = lexicon
        self.anagrams = anagrams
        self.bag = bag
        self.player = Player.Player(bag)
    # end init

    def playgame(self):
        """
        yay encapsulation, we should be able to play the game from here... we may only hope...
        what does gameplay look like?
        1. show player their tiles
        2. let them enter a word
        3. verify it's a legal play
        4. adjudicate their score
        5. adjudicate the highest possible score available on the rack.
        6. refill the rack
        7. return to #1
        """
        self.showrack()
        # solicit input and validate it
        a_play = raw_input("Please enter a word.")
        print(self.player.rack.isvalidplay(a_play), self.lexicon.find(a_play))
        if (self.player.rack.isvalidplay(a_play) and self.lexicon.find(a_play)):
            print("That is a valid play!")
        # TODO: SCREEE-KRUNCH, need to implement more game steps

    # end playgame

    def showrack(self):
        print("You have the following letters available:")
        print(self.player.rack.tiles)
