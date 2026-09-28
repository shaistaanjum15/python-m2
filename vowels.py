sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for ch in sentence:
    if ch == " ":      # only checks the spaces
        spaces += 1
    elif ch.isalpha():  # only count letters
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("\nVowels =", vowels)
print("Consonants =", consonants)
print("Spaces =", spaces)