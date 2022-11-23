def observed():
  observations=set()
  for i in range(7):
    value=input('Please enter values for set ')
    observations.add(value)
# print(observations)
  return observations

def run():
  localvar=observed()
  print("Counting observations...")
  count=0
  for i in localvar:
    print(i)

run()
