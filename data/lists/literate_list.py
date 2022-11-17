def directions():
  directions=["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print('Select a direction')
  locv=directions()
  index=0
  for index in range(len(locv)):
    print(f'{index+1} : {locv[index]}')
  
def calling():
  menu()

calling()