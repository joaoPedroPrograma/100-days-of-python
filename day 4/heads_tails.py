import random
#import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

#random_number_0_to_1 = random.random() * 10
#print(random_number_0_to_1)

#random_float = random.uniform(1, 10)
#print(random_float)
# print(my_module.my_favorite_number)
         #módulo      #função no módulo

askUser = input("Heads or Tails?").lower()
chosen = random.choice(["heads", "tails"])
if askUser == chosen:
    print("Congrats, you won!")
else:
    print("Game Over...")