#!/usr/bin/env python3

import bcrypt

default_pwd = b'Password'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(default_pwd, salt)

print('Password: %s\nHashed: %s' % (default_pwd, hashed))

password = input('Enter your password: ')

print(bcrypt.checkpw(password.encode('utf8'), hashed))