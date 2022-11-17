def sum_weights(beep_weight, bop_weight): 
  total_weight=beep_weight+bop_weight  
  return total_weight

def calc_avg_weight(beep_weight, bop_weight):
  average=(beep_weight + bop_weight)/ 2
  return average

def run():
  print('What is the weight of beep')
  beep_weight=int(input())
  print('What is the wight of bop')
  bop_weight=int(input())
  action=input("What would you like to calculate?(sum or averge)  ")
  
  var1=sum_weights(beep_weight, bop_weight)
  var2=calc_avg_weight(beep_weight, bop_weight)
  if(action == 'sum'):
    print(f"The sum of Beep and Bop's weight is {var1}")
  elif(action=='average'):
    print(f'The average weight of Beep and Bop is {var2}')
    
run()