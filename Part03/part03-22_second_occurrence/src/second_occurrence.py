# Write your solution here

word = input("Please type in a word: ")
sub =  input("Please type in a character: ")

indexWord = word.find(sub)
newWord = word[indexWord + len(sub):]
preNewWord = word[: indexWord + len(sub)]

if sub in word:


    list = [i for i in range(len(newWord)) if newWord.startswith(sub, i)]
    if len(list) == 0:
        print("The substring does not occur twice in the string.")
    else:
        x = list[0] + len(preNewWord)
        print(f"The second occurrence of the substring is at index {x}.")
else:
    print("The substring does not occur twice in the string.")