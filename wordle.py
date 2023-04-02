import words
import display_utility
import random

def check_word(secret, guess):
    '''
    Purpose:
        This function compare the user input "guess" with the word "secret" and output a list consisting of the strings "grey", "yellow"
        and "green".
    Parameters:
        secret: A five-letter long word in the wordle.
        guess: A five-letter long word given by user.
    return:
        A list consisting of five strings "grey", "yellow" and "green".
    '''
    color = ["grey", "grey", "grey", "grey", "grey"]
    for i in range(len(secret)):
        if(guess[i] == secret[i]):
            color[i] = "green"
        elif(guess[i] in secret):
            color[i] = "yellow"

    # Check the case with repeated letters
    letters = list(secret)
    for i in range(len(guess)):
        if color[i] == "yellow":
            target_letter = guess[i]
            target_count = secret.count(target_letter) # Number of target_letter in secret

            green_target_count = 0
            for j in range(len(letters)):
                if(guess[j] == letters[j] and guess[j] == target_letter):
                    green_target_count += 1

            max_yellow = target_count - green_target_count
            current_yellow_count = 0
            for k in range(i):
                if(guess[k] == target_letter and color[k] == "yellow"):
                    current_yellow_count += 1

            if(current_yellow_count == max_yellow):
                color[i] = "grey"

    return color



def known_word(clues):
    '''
    Purpose:
        Gives a string consisting of green letters and _'s.
    Parameters:
        clues: a list of tuples, with each tuple being a guess (string) and the clues returned (a list of strings,
        consisting of "green", "yellow", "grey").
    Return:
        A length five string indicating what we know about the secret word according to green hints seen so far.
    '''
    output_list =['_','_','_','_','_'] # A length five list contains letters of the output string
    output = ""
    for element in clues:
        colors = element[1]
        for color_index in range(len(colors)):
            if colors[color_index] == "green":
                output_list[color_index] = element[0][color_index]
    
    for i in range(5):
        output += output_list[i]
    return output



def no_letters(clues):
    '''
    Purpose:
        This function gives a string of letters that are not in the word.
    Parameter:
        clues: a list of tuples, with each tuple being a guess (string) and the clues returned (a list of strings,
        consisting of "green", "yellow", "grey").
    Return:
        A string of alphabetically ordered capital letters that are not in the word.
    '''
    yellows_or_greens = [] # A list stores yellow letters (with duplicates)
    greys = [] # A list stores yellow letters (with duplicates)
    output = "" # The ouput string
    for element in clues:
        colors = element[1]
        for color_index in range(len(colors)):
            if (colors[color_index] == 'yellow' or colors[color_index] == 'green'):
                yellows_or_greens.append(element[0][color_index])
    yellows_or_greens = list(set(yellows_or_greens)) # Remove duplicates

    for ele in clues:
        for index in range(len(ele[1])):
            if((ele[1][index] == 'grey') and (ele[0][index] not in yellows_or_greens)):
                greys.append(ele[0][index])
    greys = list(set(greys)) # Remove duplicates
    greys.sort() # Sort into alphabetic order

    for i in range(len(greys)):
        output += greys[i]
    
    return output



def yes_letters(clues):
    '''
    Purpose:
        This function gives a string of letters that are in the word.
    Parameter:
        clues: a list of tuples, with each tuple being a guess (string) and the clues returned (a list of strings,
        consisting of "green", "yellow", "grey").
    Return:
        A string of alphabetically ordered capital letters that are in the word.
    '''
    yellows_and_greens = [] # A kist containing yellow and green letters (with duplicates)
    output = "" # Output string
    for element in clues:
        colors = element[1]
        for color_index in range(len(colors)):
            if(colors[color_index] == "yellow" or colors[color_index] == "green"):
                yellows_and_greens.append(element[0][color_index])
    yellows_and_greens = list(set(yellows_and_greens)) # Remove duplicates
    yellows_and_greens.sort() # Sort the list into alphabetic order

    for i in range(len(yellows_and_greens)):
        output += yellows_and_greens[i]
    
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
        clue = check_word(secret, guess) # list of colors corresponding to the guess
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
        
        print("Known:", known_word(clues)) # Print known word
        print("Green/Yellow Letters:", yes_letters(clues)) # Print green/yellow letters
        print("Grey Letters:", no_letters(clues)) # Print grey letters

    print("Answer:", secret)


    
