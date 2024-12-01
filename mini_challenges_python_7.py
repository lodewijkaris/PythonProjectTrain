word = input("Geef een woord op: ")
new_word = ""

for i in range(0, len(word), 2):
    # iterating over the string, starting at 0 with a step of 2

    if i == len(word) - 1:
        # if the index is at the last character, add it to the new word
        new_word += word[i]
    else:
        # if not, switch the positions of the two letters and add them to the new word
        new_word += word[i + 1] + word[i]

print("Origineel woord:", word)
print("New woord maar dan omgedraaid:", new_word)