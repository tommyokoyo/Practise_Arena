#!/usr/bin/python3

#take word input
#word = input("Give me your sequence: ")
word = "gjsn kfbmpvt hjbou optf"
print("You gave: \n" + word)

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#highest shift level
shift_val = 25
number_of_words = len(word)

for shift_value in range(shift_val):
    print("Iteration {0}".format(shift_value))
    for i in range(number_of_words):
        if word[i] == " ":
            print(" ", end="")
        else:
            encoded_letter_position = alphabets.index(word[i])
            #print(letter_position)
            decoded_letter_position = encoded_letter_position - shift_value
            #print(original_letter)
            print(alphabets[decoded_letter_position], end="")
    print("\n")
