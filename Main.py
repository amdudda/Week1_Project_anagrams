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

# TODO build user interface
# main menu
# - check if word is valid
# - look for anagrams
# - play game

""" MAIN METHOD FUNCTIONS"""
# prints out the main menu
def show_menu():
    lines = []
    lines.append("Welcome to Anagramarama!")
    lines.append("You have some options available:")
    lines.append("\t1. Check if a word is in my dictionary")
    lines.append("\t2. Find anagrams of a word or series of letters")
    lines.append("\t3. Play Anagramarama")
    lines.append("\t4. Quit :( ")
    lines.append("> ")
    for l in lines:
        print(l)
# end show_menu

def do_menu():
    global is_valid
    is_valid = False
    while not is_valid:
        # solicit user input and act on it until we get valid input
        user_choice = raw_input()
        handle_menu_choice(user_choice)
# end do_menu

# verifies if a word is in the dictionary
def check_word():
    user_word = raw_input("Please enter a word, or leave blank to exit.\n> ")
    while user_word != "":
        if (sDict.find(user_word)):
            print(user_word + " is in the dictionary!")
        else:
            print("Sorry, " + user_word + " is not in the dictionary.")
        user_word = raw_input("Please enter a word, or leave blank to exit.")
    # return to the main menu when done
    do_menu()
# end check_word

# handles main menu user input
def handle_menu_choice(i):
    global is_valid
    if (i == '1'):
        check_word()
    if (i == '4'):
        # option 4 is "quit", so exit the program
        is_valid = True # defensive coding - let's not cause an infinite loop!
        exit()
    else:
        print("You have made an invalid selection.  Please try again.\n")
        show_menu()
# end handle_menu_choice



""" BODY OF CODE  """
# print our menu
show_menu()
do_menu()
