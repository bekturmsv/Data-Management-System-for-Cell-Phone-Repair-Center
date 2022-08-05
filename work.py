import context
from collections import Counter

from CourseWork import main

login = ""

def cost(element, index):
    row = element.strip("\n").split(",")
    return int(row[index])
    
def show_repair():
    lines = context.get_lines("repair-needed.txt")

    for i,line in enumerate(lines):
        price = line.strip("\n").split(",")[1]
        row = line.strip("\n").split(",")
        print(f"{i+1}. {row[0]}, за {price}$")

def show_service():
    lines = context.get_lines("service-need.txt")

    for i,line in enumerate(lines):
        row = line.strip("\n").split(",")
        print(f"{i+1}. {row[0]}, за {row[1]}$")

def show_change():
    lines = context.get_lines("change_need.txt")

    for i,line in enumerate(lines):
        row = line.strip("\n").split(",")
        print(f"{i+1}. Model:{row[0]}, need to replace {row[1]}, for {row[2]}$")

def show_most_expensive():
    print("1. Repair")
    print("2. Service")
    print("3. Replace")

    index = int(input("Select a category:"))

    if(index==1):
        line = max(context.get_lines("repair-needed.txt"), key=lambda x: cost(x, 1)).split(",")
        print(f"The biggest order is {line[0]} for {line[1]}$")
    if(index==2):
        line = max(context.get_lines("service-need.txt"), key=lambda x: cost(x, 1)).split(",")
        print(f"The biggest order is {line[0]} for {line[1]}$")
    if(index==3):
        line = max(context.get_lines("change_need.txt"), key=lambda x: cost(x, 2)).split(",")
        print(f"The biggest order is :{line[0]}, need {line[1]}, for {line[2]}$")

def show_cheapest():
    print("1. Repair")
    print("2. Service")
    print("3. Replace")

    index = int(input("Select a category:"))

    if(index==1):
        line = min(context.get_lines("repair-needed.txt"), key=lambda x: cost(x, 1)).split(",")
        print(f"The cheapest order is {line[0]} for {line[1]}$")
    if(index==2):
        line = min(context.get_lines("service-need.txt"), key=lambda x: cost(x, 1)).split(",")
        print(f"The cheapest order is {line[0]} for {line[1]}$")
    if(index==3):
        line = min(context.get_lines("change_need.txt"), key=lambda x: cost(x, 2)).split(",")
        print(f"The cheapest order is :{line[0]}, need {line[1]}, for {line[2]}$")

def show_stats():
    print("1. Repair")
    print("2. Service")
    print("3. Replace")

    index = int(input("Select a category:"))

    if(index==1):
        a = []
        a += context.select_only("repair-needed.txt", 0)
        a += context.select_only("repaired.txt", 0)
        count = Counter(a).most_common()[0]
        print("Most of all in the repair sector you need to do", count[0], f"(total {count[1]} orders)")

    if(index==2):
        a = []
        a += context.select_only("service-need.txt", 0)
        a += context.select_only("serviced.txt", 0)
        count = Counter(a).most_common()[0]
        print("Most of all in the service sector you need to do", count[0], f"(total {count[1]} orders)")

    if(index==3):
        a = []
        a += context.select_only("change_need.txt",0)
        a += context.select_only("changed.txt",0)
        count = Counter(a).most_common()[0]
        print("Most part replacements required model", count[0], f"(total {count[1]} orders)")

def menu_start(login_par):
    commands = [show_repair, show_service, show_change, show_most_expensive, show_cheapest, show_stats]
    global login
    login = login_par
    while True:
        print()
        print("Greetings dear, Worker !")
        print("Please dial the menu number to work with the program, if finished, then dial 7:")

        print("1. View the list of devices for repair")
        print("2. View list of devices for maintenance")
        print("3. View the list of devices, need replacement")
        print("4. Show the most expensive order for:")
        print("5. Show the cheapest order for:")
        print("6. View statistics on:")
        print("7. Exit")

        command = int(input(":"))

        if(command>7 or command<1):
            print("Error, there is no such command here, please try again :-(")
            continue
        if(command == 7):
            main.main()
            break

        commands[command-1]()
