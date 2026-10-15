# (c) Om Kanabar 2026

import random
import syllables

# This function allows you to specify an input type as well as the input, and if the user doens't enter the correct type it will ask again with the correct type.

def input_type(i_type, question):
    i = 0
    while i <= 3:
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
        i += 1

    print("Really? Even after asking nicely you still decide to enter an invalid input?")

# List of starts

one_syllable_starts = ["Oil", "Mask", "Fire", "Boat", "Death", "Light", "Rose", "Food", "We", "They", "Light", "Art", "Time", "Space", "Book"]
two_syllable_starts = ["Firelight", "Free Will", "Mother", "Teacher", "Father", "Island", "Spector", "Kronos", "Mustang", "Laptop", "Candle", "Speaker"]

def five_syllable_line():
    starts = {
        1 : one_syllable_starts,
        2: two_syllable_starts
    }
    start_list = random.randint(1,2)
    start =  random.choice(starts[start_list])
    u_adj = input_syllable("str", 4-start_list, "word ending in ing")
    u_noun = input_syllable("str", 5-start_list-syllables.estimate(u_adj), "Noun")
    print(f"{start} {u_adj} {u_noun}")
    return

def input_syllable(i_type, s_count, w_type):
    while True:
        u_input = input_type(i_type, f"Please enter a {s_count} syllable {w_type}: ")
        if syllables.estimate(u_input) == s_count:
            return u_input


five_syllable_line()