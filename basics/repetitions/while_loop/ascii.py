print('How many bars should be charged?')
bars=int(input())
charged=1
print()

while charged<bars:
  print(f"Charging: {charged * ' █'}\n")
  charged+=1
