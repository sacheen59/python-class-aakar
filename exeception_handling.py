# print(x)

# def division(x,y):
#     try:
#         return x/y
#     # except TypeError:
#     #     return "Your number must be integer"
#     # except ZeroDivisionError:
#     #     return "second number must not be zero"
#     except (TypeError, ZeroDivisionError):
#         return "your number must be in integer and second number must not be zero"
    
        

# firstnumber = int(input("Enter first number: "))
# secondnumber = int(input("Enter second number: "))

# d = division(firstnumber,secondnumber)
# print(d)

# try, except, else, finally
# x = 10
# try:
#     print(x)
# except NameError as e:
#     print(e)

# age = "10"
# name = "sachin"

# # print(age + name)

# try:
#     result = name + age
# except TypeError:
#     print("not possible to contatenate string and integer")
# else:
#     print("Else block run when try block is successed")
#     print(result)
# finally:
#     print("finally block run always")


# try:
#     print(a)
# except Exception as e:
#     print(e)


# numbers = [1,2,3,4,5,6]
# try:
#     print(numbers[6])
# except IndexError as e:
#     print(e)

x = int(input("Enter a number: "))

try:
    if x < 0:
        raise Exception("the number must not be less than zero")
    elif x == 0:
        raise Exception("The number mustnot be zero")
    elif type(x) is not int:
        raise TypeError("The number must be integer.")
except Exception as e:
    print(e)