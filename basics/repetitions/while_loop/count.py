print('How many live cables should I avoid?')
cable=int(input())
live=0

while live<cable:
  #print('Avoiding...Done!', (live+1), 'live cables avoided.')
  #print('Avoiding.. Done {} live cables avoided'.format (live+1))
  print(f'Avoiding...Done {live+1} live cables avoided')
  live+=1
  
print()
print('All live cables have been avoided.')