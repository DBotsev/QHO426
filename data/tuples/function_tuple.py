def likelihood():
  likelihoods=(50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods)
  
def run():
  new=likelihood()
  print(f'Minimum likelihood of falling: {new[0]} %')
  print(f'Maximum likelihood of falling: {new[1]} %')
  
run()