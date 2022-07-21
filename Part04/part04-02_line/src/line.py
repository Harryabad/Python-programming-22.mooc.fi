# Write your solution here

def line(int, text):
    if len(text) == 0:
        print("*"*int)
    else:
        print(text[0]*int)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")
