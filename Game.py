"""
This encapsulates the game: take a dictionary, a bunch of anagrams, and a bag of tiles, and start playing
"""
import Player,Rack,Tiles,Anagrams

class Game():
    def __init__(self,lexicon,anagrams,bag):
        self.lexicon = lexicon
        self.anagrams = anagrams
        self.bag = bag
        self.player = Player.Player(bag)
    # end init

    def playgame(self):
        # yay encapsulation, we should be able to play the game from here... we may only hope
        # debugging:
        print(self.player.rack.tiles)
        """
        what does gameplay look like?
        1. show player their tiles
        2. let them enter a word
        3. verify it's a legal play
        4. adjudicate their score
        5. adjudicate the highest possible score available on the rack.
        6. refill the rack
        7. return to #1
        """
    # end playgame
