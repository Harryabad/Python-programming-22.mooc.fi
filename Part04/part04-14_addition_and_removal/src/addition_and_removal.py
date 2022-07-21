# Write your solution here

list = []
while True:
    print(f"The list is now {list}")

    action = input("a(d)d, (r)emove or e(x)it: ")

    if action == "d":
        list.append(len(list)+1)
    
    if action == "r" and len(list) > 0:
        list.pop(-1)
    if action == "x":
        print("Bye!")
        break