from database_handler import create_table,insert_data,update_query,delete_query,select_query

print("Enter your choices: ")
print(
    """
    1. Create Database
    2. Enter the data
    3. Update Data
    4. Delete Data
    5. Retrieve Data
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
        
elif choices == 3:
    id = input("Enter the id of user to update: ")
    address = input('Enter the address of the user to update: ')
    update_query(id,address)
    print("Data updated successfully")

elif choices == 4:
    id = input("Enter the id of user to be deleted: ")
    delete_query(id)
    print("Data delete successfully")
    
elif choices == 5:
    id = input("Enter the id of user to retrieve: ")
    data = select_query(id)
    print(
        f'''
        Username = {data[1]} {data[2]}
        address = {data[4]}
        phone number = {data[3]}
        course = {data[5]}
        '''
    )
    
    


# project work (sunday)

# requirement
# create database

# table field,
# id(primary key autoincrement)
# task
# created time
# deadline
# status = pending, completed

# if status completed then delete task

# if user want to retrieve the todo list 
# todo.txt 


# table joining 
# user 
# signin user 