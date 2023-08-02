# % - возвращает остаток от деления
number = input("Enter a number, and I'll telle you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even")
elif number % 2 == 1:
    print(f"\nThe number {number} is odd")
else:
    print("ERROR!")
