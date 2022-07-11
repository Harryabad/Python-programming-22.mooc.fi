# Write your solution here
sentence = ""
word1 = ""
while True:

    word = input("Please type in a word:")
    

    if word == "end":
        break
    if word == word1:
        break
    word1 = word
    sentence += word + " "
print(sentence)
    
