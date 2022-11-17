word=input('Please enter a word: ')
#def display_box(word):
 #   print('--------------')
  #  print(f"|   {word}    |")
   # print('--------------')
#display_box(word)

def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print("| {} |".format(word))
    print("-" * num_dashes)
display_box(word)

def lower_case(word):
  print(word.lower())

lower_case(word)
  
def upper_case(word):
  print(word.upper())

upper_case(word)

def mirrored(word):
    print(f'{word} | {word[::-1]}')
      

mirrored(word)

def repeat(word):
  print('How many times to repeat? ')
  repeating=int(input())
  for index in range(repeating):
    print(upper_case(word))
    print(lower_case(word))

repeat(word)