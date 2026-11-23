num = int(input("Enter N: "))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    a = 0
    b = 1
    for _ in range(num):
        print(a)
        nxt = a + b
        a = b
        b = nxt


