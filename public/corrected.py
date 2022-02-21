from random import *
from tkinter import E
from tkinter.messagebox import QUESTION
from typing import KeysView
question_con = 0
correct_con = 0
 
def show_flashcard():
    glossary = {
    'word1': 'definition1',
    'word2': 'definition2',
    'word3': 'definition3',
    'word4': 'definition4'
}
    random_key = choice(list(glossary))
    print('Define:', random_key)
    input('Press return to see the definition')
    print(glossary[random_key])
    user_choice = input('Did you know the definition? Enter y or n.\n')
    if user_choice == 'y':
        global question_con += 1
        global correct_answer += 1
    elif user_choice == 'n':
        global question_con
    else:
        print('Incorrect Input.\n')
def main():
    exit = False

    while not exit:
        user_input = input('Enter s to show a flashcard and q to quit:\n>')
        if user_input == 'q':
            exit = True  # exiting the loop
            print("You knew the definition {} times out of{}".format(correct_answer,question_con))
        elif user_input == 's':
            show_flashcard()
        else:
        # error trapping to check for user input errors')
            print('You need to enter either q or s.')
