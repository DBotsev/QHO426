print('What strange markings do you see?')
marks=input()
print()
print('Identifying...')

strange=0
for count in range(0, len(marks), 1):
  strange = count+1
  print(f'Index {strange} :', marks[count])

print()
print('Done')