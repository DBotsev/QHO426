print('Program started')

letter=input('Please enter a letter:')
print()
if len(letter) ==1:
  print(f'The ASCII code for {letter} is: {ord(letter)}')
else:
  print('Sorry input a single character input')
print()
print('Program ended!')
