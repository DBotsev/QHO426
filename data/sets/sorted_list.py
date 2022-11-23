def observed():
  observations=[]
  for i in range(7):
    print('Please enter an observations:   ')
    user_input=input()
    observations.append(user_input)
  return observations

def run():
  print("Counting observations...")
  first_function=observed()
  set1=set()
  for i in first_function:
    data=(i, first_function.count(i))
    set1.add(data)
    
  for data in set1:
    print(f'{data[0]} observed {data[1]} times.')

run()