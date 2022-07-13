# Write your solution here

sentence = input("Please type in a sentence: ")
char = " "

indices = [i for i in range(len(sentence)) if sentence.startswith(char, i)]

print(sentence[0])

for i in indices:
    print(sentence[i+1])


