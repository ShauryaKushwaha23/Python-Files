#Conditional expression = A one line shortcut for the if-else statement (ternary operator)  X if condition else Y

num = 1
a = 6
b = 7
age = 11
temperature = -1
user_role = "admin"

#print("Positive" if num > 0 else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)