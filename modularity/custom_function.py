# def my_function():
#     print("message from my funct.")
#
#
# my_function()
# print("end of program")


# def my_sum(nr1, nr2):
#     print("sum of nr = ", nr1+nr2)


# x=20
# y=23
# my_sum(x, y)

# def my_sum(a, b):
#     return a+b
#
#
# my_sum(12, 7)
# print(my_sum(12,7))


# def s(a, b, c=100, d=200):
#     print(a, b, c, d)
#
#
# s(10, 7)
# s(10, 7, -20)
# s(10, 7, d=-20)
# s(b=10, a=7, d=-20)

# def my_function(*args, **kwargs):
#     print("my func", args, kwargs)
#
#
# my_function()
# my_function(1,2)
# my_function(1,2,c=3)
# my_function([1,2,3], ('a', 'b', 'c'), another_key=set([True, False, None]))


# def my_function(param1, param2, *args, keyword_1=None, keyword_2=None, **kwargs):
#     print(param1, param2, args, keyword_1,keyword_2, kwargs)
#
#
# my_function(1, 2, "a", keyword_1="abc", keyword_3="this goes to kwargs")


# def f(a, b, c, *args, a1, b1, c1, **kwargs):
#     print(a, b, c, args, a1,b1, c1, kwargs)
#
#
# f(*[1,2,3,4,5,6], **{"a1":1, "b1":2, "c1":3, "d1":4})

def s(n):
    if n == 0:
        return 0

    return n +s(n-1)




# result = s(5)
# print(result)





# try:
#     user_input = int(user_input)
#     result = s(user_input)
#     print(f"sum of numbers from 0 to {user_input} = {result}.")
# except ValueError as e:
#     print(f"Caught exceptiom: {e}")
# except TypeError as e:
#     print(f"Caught exceptiom: {e}")
# else:
#     print("the code in try was succ")
# finally:
#     print("i am available no mater what")
# try_numeber=1
#
#
# while True:
#     if try_numeber > 3:
#         break
#
#     elif try_numeber > 1:
#         print(f'u have  {3- try_numeber +1} tries')
#     user_input = input("give me you message: ")
#     try:
#         user_input=int(user_input)
#     except ValueError:
#         print(f'"{user_input}" is not a valid integer')
#         continue
#     else:
#         break
#
#
# if try_numeber > 3:
#     print("u not able to provide a valid int")
# else:
#     result = s(user_input)
#     print(f"sum of numbers from 0 to {user_input} = {result}.")

a = 10

def f():
   # a="abc"
    print(a)



f()

print(a)