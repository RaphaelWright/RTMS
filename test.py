def checkname(name):
  l = name.split('-')
  for k in l:
    for b in k:
      if b.isalpha() == False:
        print('name should be in the above format')
        break



