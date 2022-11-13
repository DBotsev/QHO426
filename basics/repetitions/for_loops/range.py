print('What level of brightness is required?')
brightness=int(input())

print('Adjusting brightness...')
print()

for strenght in range(2, brightness , 2):
  print(f"Beep's brightness level: {strenght * '*'}")
  print(f"Bop's brightness level: {strenght * '*'}")
  print()
print('Adjustments complete!')
print()