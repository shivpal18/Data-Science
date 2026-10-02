# a=int(input("tell me your number : "))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry there is an error as {err}")
# else:
#     print("there is no exception")
# finally:
#     print("i will run no matter what")

# print("ok i have done the division")



age = int(input("tell your age: "))
try:
    if age < 10 or age > 18:
        raise ValueError("your age must be between 10 and 18")
    else:
        print("welcome to the club")
except Exception as err:
    print(f"an error occured as {err}")

print("the club will start soon")