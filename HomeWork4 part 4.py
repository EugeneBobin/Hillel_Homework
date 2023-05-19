height = int(input("Enter height :"))
i = 0
for i in range(height):
    print(" " * (height - 1 - i) + "*" * (1 + i * 2))
    