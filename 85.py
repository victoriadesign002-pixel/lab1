number = input("Enter number: ")

number = number.zfill(4)

if number == number[::-1]:
    print(1)
else:
    print(0)
