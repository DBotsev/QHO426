def directions():
  directions=["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print('Select a direction')
  locv=directions()
  index=0
  for index in range(len(locv)):
    print(f'{index+1} : {locv[index]}')
  user_response=int(input())
  return user_response

def run():
  #route=[]
  print("Working out escape route...")
  a=menu()
  #for i in range(5):
    #route.append(menu())
  print(f"Escape route: {a}")
run()