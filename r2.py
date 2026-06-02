# Validate User Input Excercise.

username = input("Enter a username")

if len(username) > 12:
    print("Your username can't be more than 12 years")
elif not username.find(" ") == -1 :
    print("our username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
