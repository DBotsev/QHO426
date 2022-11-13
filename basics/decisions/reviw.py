print('what is the size of the parcel?')
size=input()
print('What is the weight of the parcer?')
weight=input()

if ((size=='big') and (weight=='heavy')):
  print('This parcel will be expensive to deliver')
else:
  print("This parcel will be inexpensive to deliver.")


print()


print("What shape do I have?")
shape =input()
if (shape == ('square') or shape==('rectangale') or shape==('rhombus')):
  print ("This shape is a parallelogram.")
else:
    print("This shape is not a parallelogram.")
print()