number = 63

input_num = int(input("Guess a number from 1 to 100\n> "))

while input_num != number:
    if input_num > number:
        print("Down")
    else:
        print("Up")
    input_num = int(input("Guess a number from 1 to 100\n> "))

print("Correct!")
