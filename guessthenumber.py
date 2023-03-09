import random 
n=random.randrange(1,10)
guess=int(input("enter the number:"))
while n!=guess:
    if guess<n:
        print("too low")
        guess=int(input("enter the number again:"))
    elif guess>n:
        print("Too high")
        guess=int(input("eneter the number again:"))
    else:
        break

print("you guessed right!!")
        