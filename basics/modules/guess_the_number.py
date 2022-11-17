def play_guess_the_number():
  print("Please enter the minimum value:")
  min_value=int(input())
  print("Please enter the maximum value:")
  max_value=int(input())

  import random
  random_number=random.randrange(min_value, max_value)
#print(random_number)
  print()
  print(f"I am thinking of a number between {min_value} and {max_value}.Can you guess what it is?")


  print()
  user_guess=0
  while(user_guess != random_number):
    print('Please enter your guess:')
    user_guess= int(input())
    if user_guess < random_number:
      print("Your guess is too low.")
      print('Try again')
    elif user_guess > random_number:
      print("Your guess is too high.")
      print('Try again')
    else:
      print("Congratulations! You guessed my number!")

play_guess_the_number()