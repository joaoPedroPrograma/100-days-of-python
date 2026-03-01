# Range

#for number in range(1, 11, 3):
    #print(number)

#gauss = 0
#for number in range(1, 101):
    #gauss += number
#print(gauss)

#for i in range(1,101):
#    if i%3 ==0 and i%5==0:
#        print("FizzBuzz")
#    elif i%3==0 and i%5!=0:
#        print("Fizz")
#    elif i%5==0 and i%3!=0:
#        print("Buzz")
#    else:
#       print(i)

import string
import random

letters = list(string.ascii_letters)
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

pwd = []
for i in range(nr_letters):
    pwd.append(random.choice(letters))
for i in range(nr_numbers):
    pwd.append(random.choice(numbers))
for i in range(nr_symbols):
    pwd.append(random.choice(symbols))

random.shuffle(pwd)
password = "".join(pwd)
print(f"Your password is: {password}")