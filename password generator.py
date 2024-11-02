
import random

letters=["A","B","C","D","E","F"
         ,"G","H","I","j","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

symbols=["!","#","$","%"]

numbers=["1","2","3","4","5","6","7","8","9"]

n_letters=int(input("how many letters do you want in your password: "))

n_symbols=int(input(f"how many symbols do you want in your password: "))

n_numbers=int(input(f"how many numbers do you want in your password: "))

password=""

for char in range(1,n_letters+1):
    randchar=random.choice(letters)
    password+=randchar

for char in range(1,n_symbols+1):
    randchar=random.choice(symbols)
    password+=randchar

for char in range(1,n_numbers+1):
    randchar=random.choice(numbers)
    password+=randchar

print(password)


