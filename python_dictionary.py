# dictionary
# manage complex data in python 
# key value pair
# key unique

# information = {
#     "name": "Sachin",
#     "age": 22,
#     "course":"python Django",
#     "time": "8 AM",
#     "marks": [22,33,44,55]
# }
# print(type(information))
# print(information)

# accessing dictionary data 
# print(information["name"])
# print(information["age"])
# print(information["marks"][2])

# update
# information["name"] = "Bandhana"
# print(information)

# adding item to dictionary => update()

# information.update({"color":"white","food": "momos"})
# print(information)

# information = {
#     name,age,
# }
# print(f"my")

# color food 

# information = {
#     "name": "sachin",
#     "age": 15,
# }

# print(f"My name is {information["name"]}. I am {information['age']} years old.")

# information.update({"color":"black","food":"meat"})
# print(information)

# print(information["name"])
# print(information["color"])
# get()
# print(information.get("color"))

# removing dictionary item

# pop()
student = {
    "name":"Pragya",
    "age": 18,
    "color": "black",
    "fruit": "mango"
}
# print(id(student))

# fruit = student.pop("fruit")
# print(student)
# print(fruit)

# popitem()
# last_item = student.popitem()
# print(student)
# print(last_item[1])

# clear()
# student.clear()
# print(student)

# del()
# del student
# print(student)

# student.discard("color")
# print(student)

# student.pop("food","no value")
# print(student)

# userInput
# name,age,color,food
# 3 data

# [
#     {
#         name: value,
#         age: value,
#         color: value,
#         food: value
#     },
#     {

#     },
#     {

#     }
# ]

# information = []
# for i in range(3):
#     name = input("Enter name: ")
#     age = int(input("Enter Age: "))
#     color = input("Enter favorite color: ")
#     food = input("Enter favorite food: ")
#     data = {
#         "name": name,
#         "age": age,
#         "color": color,
#         "food": food
#     }
#     information.append(f"{data}")
# print(information)

# numbers = [
#     (1,2,3),
#     (10,11,23),
#     (4,5,6),
#     (7,8,9),
#     (55,44,66),
# ]

# num = []
# for i in range(len(numbers)):
#     total_sum = sum(numbers[i])
#     num.append([numbers[i],total_sum])
# num.sort()
# print(num)

# hackerrank , leetcode

# nested dictionary

information = {
    "name": "pragya",
    "age": 21,
    "course": "python",
    "address": {
        "permanent_address": "Bharatpur-11",
        "temporary_address": "Ratnagar-10"
    }
}

# print(information["address"]["permanent_address"])
# address = information["address"]
# print(address)
# for i in address:
#     print(i)

# keys, values, items
# print(information.keys())
# for keys in information.keys():
#     print(keys)

# print(information.values())
# for values in information.values():
#     print(values)

# print(information.items())
# # (key,value)
# for key,value in information.items():
#     print(key,value)

# for (keys,values) in information.items():
#     if keys == "address":
#         print(values)


# from copy import deepcopy
# information = {
#     "name": "pragya",
#     "age": 21,
#     "course": "python",
#     "address": {
#         "permanent_address": "Bharatpur-11",
#         "temporary_address": "Ratnagar-10"
#     }
# }

# info = deepcopy(information)

# info = information.copy()

# fromkeys()

# key = ('name','age','address')
# value = "pragya"
# information = dict.fromkeys(key)
# information['name'] = "pragya"
# information['age'] = 21
# information['address'] = "ratnanagar-10"
# print(information)

student = {
    "name": "Ram",
    "age": 15,
    "grade": 10,
    "marks": {
        "English": 90,
        "Math": 80,
        "computer": 98,
        "nepali": 70
    }
}
# name = "ram"
# age = 15
# grade = 10
# average_marks = ...
# percentage = ...

# print(f"Name = {student['name']}")
# print(f"Age = {student['age']}")
# print(f"Grade = {student['grade']}")

# marks = student["marks"]

# total_sum = sum(marks.values())
# print(total_sum)
# print(total_sum/len(marks.values()))
# for values in marks.values():
#     print(values)


