import context
from CourseWork import main

login = ""
    
def repair():

    lines = context.get_lines("repair-needed.txt")

    for i,line in enumerate(lines):
        price = line.strip("\n").split(",")[1]
        row = line.strip("\n").split(",")[0]
        print(f"{i+1}. {row}, for {price} $")
    print("Which of these would you like to fix?")

    index = int(input(":"))

    context.from_to("repair-needed.txt", "repaired.txt", lines[index - 1])
    print("Great job!")



def change():

    lines = context.get_lines("change_need.txt")

    for i,line in enumerate(lines):
        row = line.strip("\n").split(",")
        print(f"{i+1}. Change {row[1]}, at the model {row[0]}, for {row[2]}$")
    print("Which of these would you like to fix?")

    index = int(input(":"))

    context.from_to("change_need.txt", "changed.txt", lines[index - 1])
    print("Great Job!")
    
def service():
    lines = context.get_lines("service-need.txt")

    for i,line in enumerate(lines):
        row = line.strip("\n").split(",")
        print(f"{i+1}. {row[0]}, for {row[1]}$")
    print("Which of these would you like to fix?")

    index = int(input(":"))

    context.from_to("service-need.txt", "serviced.txt", lines[index - 1])
    print("Great Job!")

def order_sparepart():
    order = input("Please write what spare part you would like to order:")
    context.write("DetailOrdered.txt", [order, login])
    print("Ordered!")

def show_sparepart():
    for sparepart in context.get_items_with_login("DetailOrdered.txt", login):
        print(sparepart[0])

def delete_sparepart():
    lines = context.get_items_with_login("DetailOrdered.txt", login)
    for i,sparepart in enumerate(lines):
        print(f"{i+1}. {sparepart[0]}")
    
    index = int(input("Which part would you like to remove:"))

    context.delete_line("DetailOrdered.txt", ",".join(lines[index - 1]))
    print("Deleted!")


def menu_start(login_par):
    commands = [repair, change, service, order_sparepart, show_sparepart, delete_sparepart]
    global login
    login = login_par
    while True:
        print()
        print("Greetings dear Repairman!")
        print("Please dial the menu number to work with the program, if finished, then dial 7:")

        print("1. Repair")
        print("2. Replace")
        print("3. Hand over for maintenance")
        print("4. Order materials")
        print("5. View the list of ordered equipment")
        print("6. Remove spare part")
        print("7. Exit")

        command = int(input(":"))

        if(command>7 or command<1):
            print("Error, there is no such command here, please try again :-(")
            continue
        if(command == 7):
            main.main()
            break

        commands[command-1]()
