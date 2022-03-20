# LISTE

# my_age = 12
# my_string= "random string"
#
#
# # my_list = [12, "random string", True, None, 3+2j]
# my_list = [my_age, my_string, True, None, 3+2j]
# #            0          1      2      3     4
#
# print("my_list", my_list, type(my_list))
# print("first elememnt:", my_list[0], type(my_list[0]), my_list[-5])
# print("first elememnt:", my_list[1], type(my_list[1]), my_list[-4])
# print("first elememnt:", my_list[2], type(my_list[2]), my_list[-3])
# print("first elememnt:", my_list[3], type(my_list[3]), my_list[-2])
# print("first elememnt:", my_list[4], type(my_list[4]), my_list[-1])

# my_age = 12
# my_string= "random string"
# my_list = [12, "random string", True, None, 3+2j, 7, 8, 9, 10, "c"]   # length = 10

# print("list length", len(my_list))
# print(my_list[len(my_list)-2])
# slice: my_list[start:end:step]
# print(my_list[0:2:2])
# print(my_list[1:])
# print(my_list[:-1])
# print(my_list[::2])
# print(my_list[1::2])
# print(my_list[::-1])
# print(my_list[-1:0:-1])
# a=my_list[::-1]
# print(id(my_list), id(a))
#
# a=2
# my_list=[1, a, 3]
# print('my_list', my_list, a)
# a=4
# print('my_list', my_list, a)

#
# my_list=[1,2,3]
# my_second_list=my_list[::-1]
# print("my lsit", my_list)
# print("my second list", my_second_list)
#
#
# #
# a=[1,2,3] + [4,5,6]
# print(a)
# a[3] = 20
# print(a)
# a.append(21)
# print(a)
#
# TUPLURI

# my_tuple = ()
# my_tuple = (1,2,3, 'a', 'b', 'c')
# print(my_tuple, type(my_tuple))
# print(my_tuple[0], my_tuple[-1], len(my_tuple))
# # my_tuple[3]= 29  nu se poate TypeError: 'tuple' object does not support item assignment
#
# my_list = [1,2,3]
# print('my_list', my_list, type(my_list))
# my_tuple = tuple(my_list)
# print('my_tuple', my_tuple, type(my_tuple))
#
# my_other_list = list[my_tuple]
# print('my other list', my_other_list, type(my_other_list))
# print(my_list ==my_other_list)
# print(my_list is my_other_list)

# a= [1,2,3]
# b=a
# print(a is b)
# print('a', a)
# print('b', b)
# a=[1,2,3]
# a.append(4)
# print('a', a)
# print('b', b)

# my_tuple= (1,2,3)
# id_1=id(my_tuple)
# l=list(my_tuple)
# l.append(4)
# my_tuple= tuple(l)
# id_2=id(my_tuple)
# print('my tuple', my_tuple)
# print(id_1, id_2)
#
# tuplu_2= 1,2,3
# print("tuplu 2", tuplu_2, type(tuplu_2))

# Dictionare

# my_dic = {}
# print("my_dict", my_dic, type(my_dic))

# my_dict = {
#            "key1":10,
#            "key2": "abc",
#            1: "abc",
#            (3+2j): None,
#            (1,2,3):"abc",
#            "abc":"abc",
#            }
# print(my_dict)
# my_dict[(3+2j)]= [1,2,3]
# my_dict["new_key"] = {"a":1, "b":2, "c":3}
# print(my_dict["key2"], my_dict[(3+2j)])
# print(my_dict["new_key"])
# # print(my_dict["not existing key"])
# print(" existing key", my_dict.get(" exisiting key", 100))
# print("not existing key", my_dict.get("not exisiting key", 100))
#
# student1 = {
#     "first_name":"Iulian",
#     "last_name": "Boerescu",
#     "age":10,
#     "city":"Gaesti",
# }
#
# student2 = {
#     "first_name":"Mihai",
#     "last_name": "Vladu",
#     "age":10,
#     "city":"Gaesti",
# }
#
# student3 = {**student1, **student2}
#
# print("student 3", student3, type(student3))

# a={"a": 2, "b":3, "c":4}
# b={"b": 2, "c":3, "d":4}
# print({**a, **b})

#Seturi


#y_set= set()
# my_set = {1,2,3,'a', 'bca', None, True, 3,3, 3}
# print(" my_set", my_set, type(my_set))
# print(my_set)


my_list = [1, 2, 3, 4, 4, 5]
my_set=set(my_list)
print(my_list)
print(my_set)
print(len(my_list) == len(my_set))