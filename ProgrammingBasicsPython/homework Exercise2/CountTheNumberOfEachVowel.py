# Count the Number of Each Vowel

vowel = "aeiou"
count = 0

sentence = input("Enter a sentence or just some letters: ")

for i in sentence:
    if i in vowel:
        count += 1
print(count)