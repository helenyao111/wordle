import wordle
import words
import display_utility
import random

def filter_word_list(words, clues):
    output = []
    for word in words:
        valid_word = True
        for element in clues:
            guess = element[0]
            colors = element[1]
            if wordle.check_word(word.upper(), guess) != colors:
                valid_word = False
        if valid_word:
            output.append(word)
        
    return output



if __name__ == "__main__":
    secret = random.choice(words.words).upper()
    clues = []
    guess = ""
    count = 0
    print("Known: _____")
    print("Green/Yellow Letters: ")
    print("Grey Letters: ")

    while (count < 6):
        guess = input("> ")

        while(guess not in words.words):
            guess = input("> ")
        count += 1
        
        guess = guess.upper()
        clue = wordle.check_word(secret, guess) # list of colors corresponding to the guess
        user_guess = (guess, clue)
        clues.append(user_guess)
    
        # Display colors
        for element in clues:
            colors = element[1]
            for index in range(len(colors)):
                if(colors[index] == "grey"):
                    display_utility.grey(element[0][index])
                elif(colors[index] == "yellow"):
                    display_utility.yellow(element[0][index])
                elif(colors[index] == "green"):
                    display_utility.green(element[0][index])
            print()
        
        if (guess == secret):
            break

        possible_word_list = filter_word_list(words.words, clues)
        num_possible = len(possible_word_list)
        print(num_possible, "words possible:")

        if (num_possible <= 5):
            for possible_word in possible_word_list:
                print(possible_word)
        
        else:
            print_list = random.sample(possible_word_list, 5)
            for print_ele in print_list:
                print(print_ele)

    print("Answer:", secret)
