print("How many rows should I have?")
rows = int(input())
print()

print("How many columns should I have?")
columns = int(input())
print()

for i in range(0, rows, 1):
    for j in range(0, columns, 1):
        print(":-)", end="")
    print()