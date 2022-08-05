import autorization
import user
import repair
import work
import supply

def main():
    result = autorization.menu_start()
    if(result[0]=="customer"):
        user.menu_start(result[1])
    if(result[0]=="repairer"):
        repair.menu_start(result[1])
    if(result[0]=="worker"):
        work.menu_start(result[1])
    if(result[0]=="supplier"):
        supply.menu_start(result[1])
        


if __name__ == "__main__":
    main()