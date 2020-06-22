# Logic

import random
guessed = set()
suma = 0

def get_word_to_guess():
    print('H A N G M A N')
    print()
    word_list = ['python', 'java', 'kotlin', 'javascript']
    index = random.randint(0,3)
    return word_list[index]

def create_template(word):
    template = []
    for i in range(len(word)):
        template.append('-')
    return template
        
def chech_if_letter_correct(word, template):
    global guessed, suma
    
    letter = input('Input a letter:')
    
    
    if letter in guessed:
        print("You already typed this letter")
        return False 
    elif len(tuple(letter)) != 1 :
        print("You should input a single letter") 
        return False
    elif letter.islower() == False:
        print("It is not an ASCII lowercase letter")   
        return False
    elif letter in set(word): 
        for i, l in enumerate(word):
            if letter == l:
                guessed.update(letter)
                template[i] = letter
        return False    
    else:
        guessed.update(letter)
        print('No such letter in the word')
        return True
    
   
    if suma < 8:
        suma += 1 
    
def check_winner(word, template):
    return word == template
    

# Ready to work
game = input('Type "play" to play the game, "exit" to quit:')
while game == 'play':   
    word_to_guess = get_word_to_guess()
    template = create_template(word_to_guess)
    count = 0
    while count < 8:
        print()
        print(''.join(template))
        if chech_if_letter_correct(word_to_guess, template) == True:
            count += 1

    if check_winner(word_to_guess, template) == True:
        print("You guessed the word {}!".format(word_to_guess))
        print("You survived!")
    else:
        print("You are hanged!")
        game = input('Type "play" to play the game, "exit" to quit:')
    
    if game == 'quit': 
        break
    

