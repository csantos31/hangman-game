from graphics import graphics
from random import randint
from words import words
from time import sleep
import unicodedata
import os

challenge_word = words[randint(0,len(words)-1)]
success_attempts = []
error_attempts = []

def main():
    initialize_game()

    while True:
        print_game_status()
        given_letter = get_user_input()
        end_game = proccess_attempt(given_letter)
        
        if(end_game):
            print_game_status()
            sleep(5)
            print('\nThanks for playin\'')
            clear_terminal()
            break


def initialize_game():
    for _ in challenge_word:
        global success_attempts
        success_attempts.append('_')


def print_game_status():
    print(graphics[len(error_attempts)])

    for letter in success_attempts:
        print(f'{letter}', end=' ', flush=True)
        sleep(0.3)

    print('\n')

    if(len(error_attempts) > 0):
        
        print('\n\nWRONG LETTERS\n')
        for letter in error_attempts:
            print(f'{letter}', end=' ', flush=True)
    

def get_user_input():
    return input(f'\nGive one letter\n')


def sanitize_string(input):
    n = unicodedata.normalize('NFKD', input)  
    return ''.join([c for c in n if not unicodedata.combining(c)]).upper()


def clear_terminal():
    os.system('clear')


def proccess_attempt(given_letter):
    clear_terminal()
    if (len(given_letter) != 1):
        print('Only one letter at a time and at least one letter at a time') 
        return False
    
    sanitized_word = sanitize_string(challenge_word)
    sanitized_input = sanitize_string(given_letter)

    if(sanitized_input in error_attempts
        or sanitized_input in (sanitize_string(letter) for letter in success_attempts)):
        print('You had already given this letter, please, try other')
        return False
    
    if(sanitized_input in sanitized_word):
        for index in range(len(sanitized_word)):
            if(sanitized_word[index] == sanitized_input):
                success_attempts[index] = challenge_word[index]
        if(challenge_word == ''.join(letter for letter in success_attempts)):
            print(f'\nCONGRATS! U R THE BEST, YOU WON! ! !\n THE WORD IS {challenge_word}')
            return True
        
    else:
        error_attempts.append(sanitized_input)
        if(len(error_attempts) == len(graphics)-1):
            print(f'Good luck next time...\n The word is {challenge_word}')
            return True
    return False
    
main()