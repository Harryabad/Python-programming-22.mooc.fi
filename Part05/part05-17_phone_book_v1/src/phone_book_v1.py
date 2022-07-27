# Write your solution here

### REFACTOR


def search(phonebook):
    name = input("name: ")
    if name in phonebook:
        print(phonebook[name])
    else:
        print("no number")

def add(phonebook):
    name = input("name: ")
    number = input("number: ")
    phonebook[name] = number
    print("ok!")

def main():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 1:
            search(phonebook)
        if command == 2:
            add(phonebook)
        if command == 3:
            break
    print("quitting...")

main()


# phonebook = {}

# while True:

#     command = int(input("command (1 search, 2 add, 3 quit): "))

#     if command == 3:
#         print("quitting...")
#         break
    
#     if command == 2:
#         name = input("name: ")
#         number = input("number: ")

#         phonebook[name] = number
#         print("ok!")

#     if command == 1:
#         name = input("name: ")

#         if name not in phonebook:
#             print("no number")
#             continue

#         if phonebook[name] == "":
#             print("no number")
#         else:
#             print(phonebook[name])