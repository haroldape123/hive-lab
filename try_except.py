try:
    number = int(input("Enter a number: "))
    print(number)
    
#always specify which error that you want to "except", never let all errors pass through!
except ValueError as err:
    print("Invalid Input")
    print(err)