#NOT COMMITTED TO Repository]

#Updated programs to use functions and created a program to run all programs.

import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
def run_block_a():
  print("Which program in 'Block A: Basics' do you wish to run?")
  response = input()
  if (response == "simple_message"):
    simple_message.run()
  elif (response =="multiline_message"):
    multiline_message.run()
  
def run():
  is_running = True
  while (is_running):
    print("What would you like to do?")
    print("[a] Run 'Block A: Basics' programs")
    print("[q] Quit")
    response = input()

  if(response =="a"):
    run_block_a()
  elif(response =="q"):
    break
  else:
    print("Invalid option! Please try again.")
run()



#Complete the main.py file so that it allows us to run all the programs we have created in Block A appropriately. You will need to comment out any function calls that you may have added to the programs for this week's earlier tasks. Be sure to include appropriate comments in your code
