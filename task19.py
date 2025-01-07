import random
import string
from random  import randint
import secrets
import os
import base64


print("Choose password lenght")

lenght = int(input())
print("Choose password strentgh - easy/medium/hard")
strenght = input()
type = ['easy', 'medium', 'hard']

if lenght < 8:
    #print('Lenght of password should be bigger than 8 chars')
    while lenght < 8:
        print('Lenght of password should be bigger than 8 chars')
        lenght = int(input())

if strenght == 'easy':
   print(''.join(["{}".format(randint(0, 9)) for num in range(0, lenght)]))
elif strenght == 'medium':
    print(''.join(secrets.choice(string.ascii_uppercase + string.digits)
                     for i in range(lenght)))
elif strenght == 'hard':
    print(base64.b64encode(os.urandom(lenght)).decode('utf-8')[:lenght])
else:
    print('You have written incorrect strenght - either easy/medium/hard')
    strenght = input()