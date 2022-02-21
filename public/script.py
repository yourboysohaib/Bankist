from random import *
def show_flashcard():
    "Show th user a randwom key and ask them to define it. Show the definition when the user pressess return"
keys = list(glossary)
random_key = choice(list(glossary))
print('Define:',random_key)
input('Press return to see the definition')
print(glossary[random_key])


#SETTING UP THE GLOSSARY
glossary= {
            'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3',
            'word4':'definition4'
            }
