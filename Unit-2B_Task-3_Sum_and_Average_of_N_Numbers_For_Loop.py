#Sum and average of n numbers for loop
n = int(input("Enter the number of elements: "))
total = 0.0

for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    total += num

print(f"Sum: {total}")

if n > 0:
    average = total / n
    print(f"Average: {average}")
else:
    print("Average: Undefined (no elements entered)")
