def climb_ladder(steps_remaining, steps_crossed):
  if steps_remaining>steps_crossed:
    print('"Still some way to go!"')
  else:
    print("We are almost there!")

climb_ladder(3, 5)

print()
def cross_bridge(steps):
  for i in range(0, steps,1):
    print('Crossed step.')
    if (steps>5):
      print('"The bridge is collapsing!"')
    else:
      print("we must keep going!")


cross_bridge(3)