# file handling is the process of handiling file(.txt,.csv, etc) using programming language
# write mode => if file doesnot exits it will make it and write content on that file
# read => it will read the content of the existing file 
# append => it will write the content of the existing file 

# file = open("text.txt",'r')
# # a = file.readline()
# # print(a)
# # b = file.readline()
# # print(b)
# a = file.readlines()
# print(a)
# file.close()

# file = open("my-text.txt",'a')
# # file.write("I am learning python\n")
# # file.write("We are learning more")
# # file.writelines(
# #     [
# #         "we are learning python\n",
# #         "we are doing best\n",
# #         "It's very good to learn python\n"
# #     ]
# # )
# # file.write("Hello world\n")
# file.write("we are doing best\n")
# file.close()

# user
# Name
# age
# Course

# 3 data 
# file write

# with open("my-text.txt",'r') as file:
#     a = file.read()
#     print(a)


# seek
# where to move the cursor 

with open("my-text.txt","r") as file:
    a = file.read(10)
    print(a)
    file.seek(10)
    b = file.read(6)
    print(b)