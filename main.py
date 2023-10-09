import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("huess a letter").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")