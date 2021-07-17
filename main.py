print("Enter the letter")
letter = (input())
print("Enter the number")
number = int(input())
if (letter == "a" or letter == "с" or letter == "e" or letter == "g") and number % 2 == 0:
    print("White")
elif (letter == "a" or letter == "с" or letter == "e" or letter == "g") and number % 2 != 0:
    print("Black")
if (letter == "b" or letter == "d" or letter == "f" or letter == "h") and number % 2 == 0:
    print("Black")
elif (letter == "b" or letter == "d" or letter == "f" or letter == "h") and number % 2 != 0:
    print("White")
