print("How many numbers should I sum up?")
retrived=int(input())
num=1
total=0
while num <= retrived:
  print(f'Please enter number {num} of 4')
  num+=1
  n1=int(input())
  total=total+n1

print(f'The number is {total}')

#The program should then retrieve the user's response. The program should then use a while loop to repeatedly prompt the user for a number.The specified number should be added to a running total. Finally, the program should display the message "The answer is" followed by the answer.