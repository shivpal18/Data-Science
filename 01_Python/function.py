# def hello():
#     print("This is a hello function")

# hello()



# def sum(a,b):
#     print(f"The sum of your numbers is {a+b}")

# sum(12,14)



# keyword arguments
# def hello(name, age):
#     print(f"your name is {name} and your age is {age}")

# hello(age = 20, name = "shivpal")



# def sum(a,b=23):
#     print(f"the sum is {a+b}")

# sum(12,25)



# def palindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print(f"{st} is a palindrome")
#     else:
#         print(f"{st} is not a palindrome")

# palindrome("hi")



def hello():
    return "hello"

print(hello())