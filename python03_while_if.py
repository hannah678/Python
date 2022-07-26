number = 63

input_num = int(input("1~100 사이의 숫자를 입력하세요\n> "))

while input_num != number:
    if input_num > number:
        print("Down")
    else:
        print("Up")
    input_num = int(input("1~100 사이의 숫자를 입력하세요\n> "))

print("Correct!")