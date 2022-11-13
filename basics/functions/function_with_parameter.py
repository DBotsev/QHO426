def escape_by(plan):
  if (plan == 'jumping over'):
    print('We cannot escape that way ! The boulder is too big')
  elif(plan == 'running around'):
    print('we cannot escpa that way ! The boulder is moving too fast !')
  elif plan =='going deeper':
    print('This might just work! Lets go deeper !')
  else:
    print('We cannot escape that way !')

escape_by('going deeper')
escape_by('running around')
escape_by('zzz')