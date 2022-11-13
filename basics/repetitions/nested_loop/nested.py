print('How many rows should I have?')
rows=int(input())
print()
print('How many columns should I have?')
colums=int(input())
print()

print('Here I go:')

for rows in range(0, rows, 1):
  for colums in range(0, colums, 1):
    print(':- ) ', end="")

print('Done')