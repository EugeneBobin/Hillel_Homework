x = list(input("sdf"))

if len(x) % 2 == 0:
    print([x[:int(len(x) / 2)], x[int(len(x) / 2):]])
elif len(x) % 2 != 0:
    print([x[:int(len(x) // 2 + 1)], x[int(len(x) // 2 + 1):]])
elif len(x) == 0:
    print([[], []])
