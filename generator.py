# def square():
#     for i in range(5):
#         yield i

# gen = square()

# print(next(gen))
# print(next(gen))
# print(next(gen))

def file_read(path):
    with open(path,'r') as file:
        for line in file:
            yield line.strip()

# gen = file_read("file.txt")

print(next(file_read("file.txt")))
print("---------")

print(next(file_read("file.txt")))

