"""
Implements a Rack object
"""
import random
import Tiles

class Rack():
    def __init__(self,bag):
        # draw tiles from bag
        # select a random letter of the alphabet
        self.tiles = []
        # populate the rack with tiles
        self.loadtiles(bag)
    # end init

    def playtiles(self,word):
        for l in word:
            self.tiles.remove(l)
    # end playtiles

    def loadtiles(self,bag):
        # add tiles to rack from bag
        # debugging: print(bag.tiles)
        while (len(self.tiles)<7 and bag.gettilecount() > 0):
            drawn = chr(random.randint(65, 90))
            if (drawn in bag.tiles and bag.numberof(drawn) > 0):
                # if the letter is in the bag, add it to the rack and decrement the number of that letter available.
                self.tiles.append(drawn)
                bag.decrementtile(drawn)
    # end loadtiles

    def isvalidplay(self, playerword):
        # verify the play uses only letters drawn from the rack
        # copy the array so the original one is intact
        playerword = playerword.upper()
        avail = self.tiles[:]
        for letter in playerword:
            if letter not in avail:
                return False
            else:
                avail.remove(letter)
        # if we get past all that, it's a valid play as far as the rack cares and we can return true.
        return True

