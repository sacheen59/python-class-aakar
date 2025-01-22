import sqlite3

connection = sqlite3.connect("user_db.db")
cursor = connection.cursor()

print('Database created successfully')


# function to create table in database 
def create_table():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tb_user (
            id integer PRIMARY KEY AUTOINCREMENT,
            firstname varchar(200),
            lastname varchar(200),
            phone_number varchar(200),
            address varchar(200),
            course varchar(100)
        )
        '''
    )
    connection.commit()
    connection.close()
    print("Table created successfully.")

def insert_data(**kwargs):
    insert_query = '''
        INSERT INTO tb_user (
            firstname,
            lastname,
            address,
            phone_number,
            course
        )
        VALUES (?,?,?,?,?)
        '''
    values = (kwargs['firstname'],kwargs['lastname'],kwargs['address'],kwargs['phone_number'],kwargs['course'])
    cursor.execute(insert_query,values)
    connection.commit()

def update_query(id,address):
    cursor.execute(
        "UPDATE tb_user SET address = ?  WHERE id = ?",
        (address,id)
    )
    connection.commit()
    connection.close()

def delete_query(id):
    cursor.execute('DELETE FROM tb_user WHERE id = ?',(id))
    connection.commit()
    connection.close()
    
def select_query(id):
    cursor.execute('SELECT * from tb_user WHERE id = ?',(id))
    data = cursor.fetchone()
    return data
    
