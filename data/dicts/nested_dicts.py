def short_pattern():
  pattern={"sequence":101, "occurrences":5}
  return pattern
  
def medium_pattern():
  pattern={"sequence":"111000", "occurrences":25}
  return pattern

def long_pattern():
  pattern={"sequence":"1100110011001100", "occurances":50}
  return pattern

def run():
  print("Analysing patterns...")
  newdict={'short sequence': short_pattern(), 'medium_pattern': medium_pattern(), 'lond_pattern': long_pattern()}
  for a,b in newdict.items():
    print(f'{a} : {b}')
  
    
run()