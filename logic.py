import data as d
# from data import username,password,greet

user = input("Enter username: ")
secure_key = input("Enter password: ")

def sigin(name,pas):
    if name in d.username and pas == d.password:
        return 'login successful'
    else:
        return "login failed"
    
print(sigin(user,secure_key))