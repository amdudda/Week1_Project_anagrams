import Dictionary, Anagrams, Tiles

# this file is uploaded from the Moby Words project; see http://icon.shef.ac.uk/Moby/mwords.html for details
wordlist = "scrabble.txt"

# build my dictionary
sDict = Dictionary.dictionary(wordlist)
# debugging: print(sDict.words[1])
# debugging: print(sDict.find("zxzxz"))

# build my anagram cohort dictionary
aDict = Anagrams.anagrams(sDict.words)

# build my bag of tiles
bag = Tiles.tile_bag()
#debugging: print('z: ' + str(bag.valueof('z')))