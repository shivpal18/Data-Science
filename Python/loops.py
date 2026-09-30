# For loop

# for i in range(1,21,1):
    # print(i)


# print a table
# n = int(input("Which table you want ?"))
# for i in range(n,(n*10)+1,n):
    # print(i)


# loop in string
# a = "SHIVPAL CHAURASIYA"
# for i in range(len(a)):
#     print(a[i])


# break statement in for loop
# for i in range(1,21):
#     if i ==15:
#         break
#     print(i)


# continue statement in for loop
# for i in range(1,21):
#     if i ==15:
#         continue
#     print(i)


# else statement in for loop
# for i in range(1,21):
#     if i ==156:
#         print("break statement is exucuted")
#         break
#     print(i)
# else:
#     print("break statement is not executed")


# while loop
# a=1
# while a <= 30:
#     print(a)
#     a = a+1


# a = int(input("tell your number: "))
# while a > 0
#     print(a % 10)
#     a = a // 10



# A random number guessing game 
import random
num = random.randint(1,10)

tries = 0

while True:
    guess = int(input("Please guess a number between 1 and 10 :- "))
    if num == guess:
        tries += 1
        print(f"You are right you guessed the number is {tries} tries")
        break

    elif num < guess:
        print("go a little lower")
        tries += 1

    elif num > guess:
        print("go a little higher")
        tries += 1

    else:
        tries += 1
        print("sorry you are wrong")