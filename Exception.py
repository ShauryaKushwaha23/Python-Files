# exception = An event interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can devide by zero Idiot !")
except ValueError:
    print("Enter your numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some clean up here")