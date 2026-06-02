#Return = statement used to end a function and send a result back to the caller.

#def add(x, y):
 #   z = x + y
  #  return z

#def subtract(x, y):
 #   z = x - y
  #  return z

#def multiply(x, y):
 #   z = x * y
  #  return z

#def divide(x, y):
 #   z = x / y
  #  return z

#print(add(1, 2))
#print(subtract(4, 2))
#print(multiply(4,2))
#rint(divide(4, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("shaurya", "kushwaha")

print(full_name)