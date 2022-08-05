import context
import uuid

from CourseWork import main

login = ""

def show_all_services():
    print("We can fix your device, replace a component, service your equipment!")

def give_to_repair():
    print("Please select a category of equipment for repair")

    print("1) Repair the display - 50$")
    print("2) Fix the keyboard -25$")
    print("3) Repair internals (motherboard, processor, etc.) -40$")

    choose = int(input(":"))

    if (choose > 3 and choose < 1):
        print("There is no such service")
        return

    services = [
        ("Repair the display", 50),
        ("Fix the keyboard", 25),
        ("Fix the insides ", 40)
    ]
    id = uuid.uuid4()
    service = services[choose-1][0]
    price = services[choose - 1][1]
    print("Your order has been successfully accepted")

    context.write("repair-needed.txt", [service, price, login, id])
    print("Your serial number", id)

def change():
    print("Choose what you want to replace in your technique? >>>")

    services = [
        ("Battery", 15),
        ("Display", 25),
        ("CPU",45),
        ("Motherboard", 85),
        ("RAM", 15)
    ]

    for i,v in enumerate(services):
        print(f"{i+1})",v[0],f"за {v[1]}$")

    choose = int(input(":"))

    if (choose > 5 and choose < 1):
        print("There is no such service")
        return

    id = str(uuid.uuid4())
    service = services[choose-1][0]
    price = services[choose-1][1]

    print("Select the technique in which you want to replace the material:")

    print("1) Apple - 3 coefficient")
    print("2) Samsung - 2.5 coefficient")
    print("3) Xiomi - 1.8 coefficient")
    print("4) Huawei - 2.3 coefficient")

    choose = int(input(":"))
    models = [("Apple",3), ("Samsung", 2.5), ("Xiomi", 1.8), ("Huawei", 2.3)]

    if (choose > 4 and choose < 1):
        print("There is no such service")
        return

    model = models[choose-1][0]
    price = int(models[choose-1][1]*price)
    print("Your order has been successfully accepted")

    context.write("change_need.txt", [model, service, price, login, id])
    print("Your serial number ", id)

def service():
    print("Select the type of service")
    services = [("Dust cleaning", 10),("Cleaning from scratches", 1)]
    for i,serv in enumerate(services):
        print(f"{i+1}) {serv[0]} за {serv[1]}$")
    service = int(input(":"))
    print("Your order has been successfully accepted")
    id = str(uuid.uuid4())
    if(service > 2 and service <1):
        print("There is no such service")
        return

    context.write("service-need.txt", [services[service - 1][0], services[service - 1][1], login,id])
    print("Your serial number ", id)

def model_in_file(serial, file_needed, file_end,index):

    for row in context.get_items_by_login(file_needed, serial):
        if (row == serial):
            return "Your device is not ready yet"

    for row in context.get_items_by_login(file_end, serial):
        if (row == serial):
            return "Your device is ready!"

    return "We didn't find anything like that, sorry"
    
def check_status():
    print("What do you want to check:")
    print("1) Repair")
    print("2) Service")
    print("3) Replacement")
    section = int(input(":"))
    serail = input("Enter the serial number:")
    if(section<4 and section>0):
        if(section==1):
            print(model_in_file(serail, "repair-needed.txt", "repaired.txt",index = 3))
        if(section==2):
            print(model_in_file(serail, "service-need.txt", "serviced.txt",index=3))
        if(section==3):
            print(model_in_file(serail, "change_need.txt", "changed.txt",index= 4))

def menu_start(login_par):
    lines = '----------------------------'
    commands = [show_all_services, give_to_repair, change, service, check_status]
    global login
    login = login_par
    while True:
        print()
        print("Greetings dear, Client!")
        print("Please dial the menu number to work with the program, if finished, then dial 6:")

        print("---1. Show all services---")
        print(lines)
        print("---2. Send for repair---")
        print(lines)
        print("---3. Replacing a component---")
        print(lines)
        print("---4. Service---")
        print(lines)
        print("---5. Check status---")
        print(lines)
        print("---6. Exit---")

        command = int(input(":"))

        if(command>6 or command<1):
            print("Error, there is no such command here, please try again :-(")
            continue
        if(command == 6):
            main.main()
            break

        commands[command-1]()
