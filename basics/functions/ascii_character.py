#range(start, stop(-1), increment/step)


print('Program started')
print('Please enter a ASCII code:')
code=int(input())
print()
if (code in range(32,127)):
#if (code not in range(32,127)):
  #if (code >=32 and code<=126):
  print(f'The character represented by the ASCII code {code} is: {chr(code)}')
else:
  print('Please enter number between 32 and 126')
print()
print('Program ended!')