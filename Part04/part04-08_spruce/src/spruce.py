# Write your solution here
# You can test your function by calling it within the following block
def spruce(num):
    print("a spruce!\n")
    
    for i in range(1,num+1,1):
        print(" "*(num-i) + "*"*(i-1) + "*" + "*"*(i-1))
    print(" "*(num-1) + "*")

if __name__ == "__main__":
    spruce(5)
