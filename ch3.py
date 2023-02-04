def right_justify(string):
    x = len(string)
    y = 70-x
    print(" "*y , string)


string = input("Enter word")
right_justify()

