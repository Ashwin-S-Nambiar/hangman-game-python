import random
from collections import Counter

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# Randomly choose a secret word from the List
word = random.choice(someWords)

if __name__ == '__main__':
    print('\nGuess the word! HINT: Word is a name of a fruit')

    for i in word:
        print('_',end=' ')
    print()

    playing = True
    letterGuessed = '' #list for storing the letters guessed by player
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances !=0) and flag == 0: 
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!') 
                continue
            #Validation of the guess
            if not guess.isalpha():
                print('Enter only a letter')
                continue
            elif len(guess) > 1:
                print('\nYou have already guessed that letter')
                continue   

            # If letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                for _ in range(k): 
                    letterGuessed += guess  # The guess letter is added as many times as it occurs 

            for char in word: 
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                    print(char, end=' ') 
                    correct += 1

                elif (Counter(letterGuessed) == Counter(word)): 
                    # the game ends, even if chances remain                                             
                    print("\nThe word is: ", end=' ') 
                    print(word) 
                    flag = 1
                    print('\nCongratulations, You won!') 
                    break  # To break out of the for loop 
                    break  # To break out of the while loop 
                else: 
                    print('_', end=' ')      

        if chances <= 0 and (Counter(letterGuessed) != Counter(word)): 
            print() 
            print('\nYou lost! Try again..') 
            print('The word was {}'.format(word)) 
  
    except KeyboardInterrupt: 
        print() 
        print('\nBye! Try again.') 
        exit()                