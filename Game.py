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
        # debugging:
        print(self.player.rack.tiles)