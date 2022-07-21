# Copy here code of line function from previous exercise
def line(int, text):
    if len(text) == 0:
        print("*"*int)
    else:
        print(text[0]*int)

def triangle(size, char):
    # You should call function line here with proper parameters
    i = 1 
    while i <= size:
        line(i, char)
        i += 1

def square(size, character):
    # You should call function line here with proper parameters
    line(size, character)

def shape(tSize, tChar, sSize, sChar):
    triangle(tSize, tChar)

    for i in range(sSize):
        square(tSize, sChar)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")