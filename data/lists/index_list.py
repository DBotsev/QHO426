def movements():
  path=["Move Forward", 10, "Move Backward", 5, "Move left", 3, "Move right", 1]
  return path

def run():
  print('Moving...')
  returned_list=movements()
  for steps in range(0, len(returned_list), 2):
    print(f'{returned_list[steps]} for {returned_list[steps+1]} steps')
      
run()