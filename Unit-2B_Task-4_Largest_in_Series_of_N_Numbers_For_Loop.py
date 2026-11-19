n = int(input("Enter the number of elements: "))

if n <= 0:
    print("Please enter a positive number of elements.")
else:
    largest = float(input("Enter number 1: "))

    for i in range(1, n):
        num = float(input(f"Enter number {i + 1}: "))
        if num > largest:
            largest = num

    print("The largest number is:", largest)
