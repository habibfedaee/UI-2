
def login(name, password):
  name = input('Please enter your name: ')
  password = input('Please enter your password: ')

  if name=='habib':
    if password == '1243':
      login=True
    else:
      login = False
   return login
  
