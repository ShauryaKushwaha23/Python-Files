#List comprehension = A concise way to create lists in python compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

#doubles = []
#for x in range(1, 11):
#    doubles.append(x * 2)

#print(doubles)

#doubles = [x * 2 for x in range(1, 11)]
#triples = [y * 3 for y in range(1, 11)]

#print(triples)

#fruits = ["apple", "orange", "banana", "coconut"]
#fruit_chars = [fruit[0] for fruit in fruits]
#print(fruit_chars)

#numbers = [1, -2, 3, -4, 5, -6]
#positive_nums = [num for num in numbers if num >= 0]
#negative_nums = [num for num in numbers if num < 0]

#print(negative_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)