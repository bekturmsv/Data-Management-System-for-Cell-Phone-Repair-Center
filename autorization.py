
import hashlib

def get_password_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def auth(login, password, account_type, file_lines):
    for line in file_lines:
        line = line.split()
        if(line[0]==login and line[1]==get_password_hash(password) and line[2]==account_type.lower()):
            return True
    return False

def menu_start():
    lines = []
    account_types = ["customer", "repairer", "worker", "supplier"]

    enter = input("1. Login \ 2. Registration : ")

    line = '----------------------------'

    if enter == '2':
        register()

    with open("users.txt", encoding='utf-8') as file:
        lines = file.readlines()

    while True:
        print()
        print("To run the program, please enter your account type: >>>")
        print(line)
        print("1.Customer")
        print(line)
        print("2.Repairer")
        print(line)
        print("3.Worker")
        print(line)
        print("4.Supplier")
        print(line)
        
        account_type = input("Enter your account type: ")
       
        if account_type == '1':
            acc_type = 'customer'
        elif account_type == '2':
            acc_type = 'repairer'
        elif account_type == '3':
            acc_type = 'worker'
        elif account_type == '4':
            acc_type = 'supplier'
        else:
            print("Sorry, but we did not find this type of account, please repeat")
            continue
        
        login = input("Enter your login:")
        password = input("Enter your password:")

        result = auth(login, password, acc_type, lines)

        if(result):
            return [acc_type.lower(), login] # Возвращаем тип аккаунта и логин
        else:
            print("Invalid username or password, please try again")


def register():
    account_types = ["customer", "repairer", "worker", "supplier"]
    line = '----------------------------'
    print("1.Customer")
    print(line)
    print("2.Repairer")
    print(line)
    print("3.Worker")
    print(line)
    print("4.Supplier")
    print(line)
    account_type = input("Enter your account type:")

    acc_type = ''
    if account_type == '1':
        acc_type = 'customer'
    elif account_type == '2':
        acc_type = 'repairer'
    elif account_type == '3':
        acc_type = 'worker'
    elif account_type == '4':
        acc_type = 'supplier'
    else:
        print("Sorry, but we did not find this type of account, please repeat")
        return

    login = input("Enter your login:")
    password = input("Enter your password:")

    with open("users.txt", "a", encoding='utf-8') as file:
        file.write(f"{login.lower()} {hashlib.sha256(password.encode('utf-8')).hexdigest()} {acc_type.lower()} \n")

    with open("users-without-hash.txt", "a", encoding='utf-8') as file:
        file.write(f"{login.lower()} {password} {acc_type.lower()} \n")



if (__name__ == "__main__"):
    register()