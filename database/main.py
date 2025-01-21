from database_handler import create_table,insert_data

print("Enter your choices: ")
print(
    """
    1. Create Database
    2. Enter the data
    """
)

choices = int(input("Enter your choices: "))

if choices == 1:
    create_table()
elif choices == 2:
    while True:
        firstname = input("Enter your firstname: ")
        lastname = input("Enter your lastname: ")
        address = input("Enter your address: ")
        phone_number = input("Enter your phone number: ")
        course = input("Enter your course: ")
        insert_data(firstname = firstname,lastname = lastname,address =address,phone_number = phone_number, course = course)
        print("*******Data inserted successfully*******")