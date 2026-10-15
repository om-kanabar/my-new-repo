# (c) Om Kanabar 2026

import random
import syllables

# This function allows you to specify an input type as well as the input, and if the user doens't enter the correct type it will ask again with the correct type.

def input_type(i_type, question):
    while True:
        user_input = input(question)
        if i_type == "str":
            return user_input
        elif i_type == "int":
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif i_type == "float":
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input. Please enter a float.")

# List of starts

one_syllable_starts = ["Oil", "Mask", "Fire", "Boat", "Death", "Light", "Rose", "Food", "Light", "Art", "Time", "Space", "Book"]
two_syllable_starts = ["Firelight", "Free Will", "Mother", "Teacher", "Father", "Island", "Spector", "Kronos", "Mustang", "Laptop", "Candle", "Speaker", "Virus"]
three_syllable_starts = ["He Started", "They Started", "We Started", "I started", "Do not start", "Microwave", "Axiom", "Armament", "Artifact", "Capitol", "Chicago"]
four_syllable_starts = ["Ephemeral", "Bacteria", "Antivirus", "Photographer", "Propoganda", "Simulator", "Solitary", "Politician", "Ontology", "Malaria", "Intelligent"]

def five_syllable_line():
    starts = {
        1 : one_syllable_starts,
        2: two_syllable_starts
    }
    start_list = random.randint(1,2)
    start =  random.choice(starts[start_list])
    u_adj = input_syllable("str", 4-start_list, "word ending in ing")
    u_noun = input_syllable("str", 5-start_list-syllables.estimate(u_adj), "Noun")
    return f"{start} {u_adj} {u_noun}"
    return


def seven_syllable_line():
    starts = {
        2: two_syllable_starts,
        3: three_syllable_starts,
        4: four_syllable_starts
    } 
    start_list = random.randint(2,4)
    start = random.choice(starts[start_list])
    u_input = input_syllable("str", 7-start_list, "phrase or word")
    return start+" "+u_input

def input_syllable(i_type, s_count, w_type):
    while True:
        u_input = input_type(i_type, f"Please enter a {s_count} syllable {w_type}: ")
        if sum(syllables.estimate(word) for word in u_input.split()) == s_count:
            return u_input



def haiku():
    line_1 = five_syllable_line()
    line_2 = seven_syllable_line()
    line_3 = five_syllable_line()
    name = input_type("str", "What's your name? ")
    print(f'"A Random Poem"\n\n\x1B[3m{line_1}\n{line_2}\n{line_3}\x1B0m]\n\n-{name}')


haiku()