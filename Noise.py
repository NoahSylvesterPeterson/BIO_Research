from random import random
def flip(i,s):
    if s[i] == "0":
        return("1")
    else:
        return "1"


def Distortion1(n,s):
    oupt = ""
    for i in range(len(s)):
        if i % n == 0:
            oupt += flip(i,s)
        else:
            oupt += s[i]
    return(oupt)
        


def Distortion2(p,s):
    oupt = ""
    for i in range(len(s)):
        if random() <= p:
            oupt += flip(i,s)
        else:
            oupt += s[i]
    return(oupt)

"""from py_thesaurus import Thesaurus

input_word = "dream"

new_instance = Thesaurus(input_word)

# Get the synonyms according to part of speech
# Default part of speech is noun

print(new_instance.get_synonym()) 

print(new_instance.get_synonym(pos='verb'))

print(new_instance.get_synonym(pos='adj'))

# Get the definitions 

print(new_instance.get_definition())

# Get the antonyms 

print(new_instance.get_antonym())"""