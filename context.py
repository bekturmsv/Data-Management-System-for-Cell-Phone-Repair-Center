def get_items_by_login(file_name, login, sep=",", index=-1):
    result = []
    with open(file_name, encoding='utf-8') as file:
        for line in file.readlines():
            if (line.split(sep)[index].replace("\n", "") == login):
                serial = line.split(sep)[index].replace("\n", "")

                result.append(serial)
    return result

def get_items_with_login(file_name, login, sep=",", index=-1):
    result = []
    with open(file_name, encoding='utf-8') as file:
        for line in file.readlines():
            if(line.split(sep)[index].replace("\n","")==login):
                result.append(line.split(sep))
    return result

def write(file_name, param_list, sep=","):
    param_list = list(map(str,param_list))
    with open(file_name, "a", encoding='utf-8') as file:
        file.write(sep.join(param_list)+"\n")

def from_to(file_need,file_end,line):
    delete_line(file_need, line)
    write(file_end, [line])

def delete_line(file, line):
    lines=[]
    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
    with open(file, "w",encoding='utf-8') as f:
        for row in lines:
            if(row.strip("\n") != line.strip("\n")):
                f.write(row)

def get_lines(file):
    with open(file, encoding='utf-8') as f:
        return f.readlines() 

def select_only(file_name, index, sep=","):
    return[ select.split(sep)[index]
        for select in get_lines(file_name) 
    ]