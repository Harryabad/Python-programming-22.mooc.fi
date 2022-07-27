# Write your solution here

def histogram(word: str):
    letters = {}

    for letter in word:

        # if the word is not yet in the dictionary, initialize the value to zero
        if letter not in letters:
            letters[letter] = 0
            
        # increment the value
        letters[letter] += 1

    for key, value in letters.items():
        print(f"{key} {value*'*'}")

    #return letters

if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")