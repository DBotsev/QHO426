def likelihood():
  likelihoods=(50, 38, 27, 99, 4)
  return min(likelihoods)

def run():
  new_like=likelihood()
  print(f"Minimum likelihood of falling: {new_like} %")
  
run()