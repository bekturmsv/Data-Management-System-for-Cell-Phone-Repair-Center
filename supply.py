import context
import main
import datetime
login = ""

def show_details():
    for line in context.get_lines("DetailOrdered.txt"):
        row = line.split(",")
        print("Material order",row[0],"for the repairman", row[1])

def deliver_detail():
    a = input("Please enter the name of the material to be delivered:")
    b = input("Please write the quantity for delivery:")

    context.write("delivered_materials.txt", [datetime.date.today(),a, b, login])

def show_delivered():
    for row in context.get_items_with_login("delivered_materials.txt", login):
        print("You delivered",row[1],"in quantity", row[2],',',"date:",row[0])

def menu_start(login_par):
    commands = [show_details, deliver_detail, show_delivered]
    global login
    login = login_par
    while True:
        print()
        print("Greetings dear Supplier!")
        print("Please dial the menu number to work with the program, if finished, then dial 4:")

        print("1. Show complete list of ordered parts")
        print("2. Deliver material:")
        print("3. Show delivered materials")
        print("4. Exit")

        command = int(input(":"))

        if(command>4 or command<1):
            print("Error, there is no such command here, please try again :-(")
            continue
        if(command == 4):
            main.main()
            break

        commands[command-1]()
