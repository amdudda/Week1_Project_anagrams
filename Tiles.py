"""
This lets us store a bag of tiles.
For now, hard code the key-value pairs, but eventually we'd want to import a file,
so that the game could be played in other languages.
"""

class tile_bag():
    # this holds a dictionary, one letter for each alphabet, and stores the number of tiles and its value in a list.
    # I'm using the Scrabble distribution - see https://en.wikipedia.org/wiki/Scrabble_letter_distributions#English
    def __init__(self):
        # build our bag of tiles
        # TODO should this be an array of Letter objects instead?
        self.tiles = {'E' : [12, 1], 'A' : [9, 1], 'I' : [9, 1], 'O' : [8, 1], 'N' : [6, 1], 'R' : [6, 1],
                      'T' : [6, 1], 'L' : [4, 1], 'S' : [4, 1], 'U' : [4, 1], 'D' : [4, 2], 'G' : [3, 2],
                      'B' : [2,3], 'C' : [2,3], 'M' : [2,3], 'P' : [2,3], 'F' : [2, 4], 'H' : [2, 4],
                      'V' : [2, 4], 'W' : [2, 4], 'Y' : [2, 4], 'K' : [1, 5], 'J' : [1, 8], 'X' : [1, 8],
                      'Q' : [1, 10], 'Z' : [1, 10]}

    def valueof(self,l):
        # return the value of a given letter - make sure we convert the character to uppercase
        l = l.upper()
        return self.tiles[l][1]

    def numberof(self,l):
        # returns the number of tiles of that letter currently in the bag - make sure we convert the character to uppercase
        l = l.upper()
        return  self.tiles[l][0]

    def wordscore(self,word):
        # returns the score of a set of letters
        # TODO does this really belong here, or in another object/method?
        # TODO - check that the word is valid!
        score = 0
        for letter in word:
            score += self.valueof(letter)
        return score