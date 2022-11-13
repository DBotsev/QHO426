print('What type of cover does the book have?')
cover=input()
print()
if cover==('soft'):
  print('Is the book perfect-bound?')
  bound=input()
  if bound==('yes'):
    print('Soft cover, perfect bound books are very popular!')
    print()
elif cover==('hard'):
  print("Books with hard covers can be more expensive!")
