secret = "MORON"


def wordle(entry):

    word = entry.upper()
    ogList = list(secret)
    newList = list(word)

    common = []
    correct = []

    if ogList == newList:  # If the user inputs the correct answer, the program ends
        for i in range(5):
            print("\033[1;32m"+newList[i]+"\033[0;0m", end=" ")
        print()
        print("Congrats! That was the right word.")
        exit()

    for i in range(5):
        # If the letters are in the right place, they are considered correct
        if newList[i] == secret[i]:
            correct.append(newList[i])

        # If the letters are not in the right place, but in the answer, they are common
        elif newList[i] in ogList:
            common.append(newList[i])

    for i in range(5):
        if newList[i] in correct:
            print("\033[1;32m"+newList[i]+"\033[0;0m",
                  end=" ")  # Prints in green
            correct.remove(newList[i])  # Remove once printed

        elif newList[i] in common:
            print("\033[1;33m"+newList[i]+"\033[0;0m",
                  end=" ")  # Prints in yellow
            common.remove(newList[i])  # Remove once printed

        else:
            print(newList[i], end=" ")  # Prints in no color

    print()


def isValid(word):
    '''
    This function checks whether the user input is a valid english word.
    The text file "valid_wordle_words.txt" must be present in the same directory as the script.
    '''
    with open("valid_wordle_words.txt") as f:  # Creates a set of all valid words
        word_list = set(word.strip().lower() for word in f)

    word = word.lower()  # All words are in lowercase
    if len(word) == 5 and (word in word_list): # Ignore words that do not have exactly 5 letters and check if word is valid in the english language
        return True
    else:
        return False


def main():
    print("Enter a 5 letter word: ")
    i = 0
    # while (i < 6):
    #     word = input()
    #     if len(word) != 5:  
    #         print("Only 5-letter words are allowed.")
    #         continue
    #     if not isValid(word):  # 
    #         print("Not in word list.")
    #         continue
    #     wordle(word)
    #     i += 1
    # else:
    #     print("The word was "+secret)


if __name__ == "__main__":
    main()
