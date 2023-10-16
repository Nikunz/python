import time

username = 'Nikunz'
password = 'login success'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Please wait')
    time.sleep(5)
    print('Ok...')
    time.sleep(1)
    print('loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Access granted')
    print('Alright you have security clearance. Pulling up the secret mainframe.')
elif username_input == username and password_input != password:
    print('Password incorrect')
elif username_input != username and password_input == password:
    print('Username incorrect')
else:
    print('You might wanna check both fields...')