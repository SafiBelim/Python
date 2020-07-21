a=int(input('Enter 1st number'))
b=int(input('Enter 2nd number'))
try:
    print("resources opened")
    print(a/b)
    k=int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e: # handling divide by zero exception
    print("Number cannot divide by zero:",e) # e for display msg of exception
except ValueError as e: # handling value error exception
    print("Invalid Input")
except Exception as e: # Hndling default exception
    print("Something went wrong.")
#finally: # it always execute
#    print("Resources closed")
print("Bye")
