"""
This builds a tool that maps words to their anagram cohort
words are rearranged so all letters appear alphabetically, and then the word is stored in a list with
all other words that rearrange to the same alphabetic sequence.  The alphabetic sequence will be the
key for a dictionary lookup.
"""

class anagrams():
    def __init__(self,lexicon):
        # create our dictionary
        self.cohort = {}
        for w in lexicon:
            # alphabetize the letters in our word to generate our key
            k = alphabetize(w)
            # if the key already exists, add the word to the list, otherwise, create a new key-value pair with the word
            # as the first element in the list
            if (k in self.cohort):
                self.cohort[k].append(w)
            else:
                self.cohort[k] = [w, ]




def alphabetize(w):
    # takes a word and rearranges its letters alphabetically - taking advantage of list.sort() in Python
    letters = []
    for l in w:
        letters += l
    letters.sort()
    # for now, until I decide whether I want a string or a tuple for my key, join as a string and return that.
    return ''.join(letters)