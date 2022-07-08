# Write your solution here
password1 = input("Password: ")
password2 = input("Repeat password: ")
while True:
    if password1 != password2 :
        print("They do not match!")
        password2 = input("Repeat password: ")
    else:
        break
print("User account created!")

