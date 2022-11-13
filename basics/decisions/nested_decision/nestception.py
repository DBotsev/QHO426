print('Where should I look?')
where=input()
if where==('in the bedroom'):
  print("Where in the bedroom should I look?")
  where_bedroom=input()
  if where_bedroom == ('under the bed'):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery.")

if where==('in the bathroom'):
  print('Where in the bathroom should I look')
  where_bathroom=input()
  if where_bathroom == ('in the bathtub"'):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery.")

else:
  print('I do not know where that is but I will keep looking')