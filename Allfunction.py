import os.path
import sys
from os import path
def get_intgr(p):
    for i in range(3):
        p = input("enter the employee_id: ")
        if p.isdigit():
            emp_id = p
            return emp_id
        else:
            print("please Enter the correct Id\nYou are left with", (3-(i+1)), "Attempts.")
    print("Please Try Again Later")
    sys.exit()
def check_name(d):
    for i in range(3):
        d = input("Enter the name of the employee: ")
        if d.isalpha():
            name = d
            return name
        else:
            print("Please Enter a Valid Name\nYou are left with", (3-(i+1)), "Attempts.")
    print("Please Try Again Later")
    sys.exit()
def check_basic(f):
    for i in range(3):
        f = input("Enter Basic Salary: ")

        if f.isdecimal():
            basic = f
            return basic
        else:
            print("Please Enter a Valid Number\nYou are left with", (3 - (i + 1)), "Attempts.")
    print("Please Try Again Later")
    sys.exit()

def check_da(g):
    for i in range(3):
        g = input("Please enter Da: ")
        if g.isdecimal():
            da = g
            return da
        else:
            print("Please Enter a Valid Number\nYou are left with", (3 - (i + 1)), "Attempts.")
    print("Please Try Again Later")
    sys.exit()
def check_gender(h):
    for i in range(3):
        g = input("Enter The gender (m/f):  ")
        if g == 'f' or g == 'm':
            gender = g
            return gender
        else:
            print("Please Enter a valid Entry\nYou are left with", (3 - (i + 1)), "Attempts.")
    print("Please Try Again Later")
    sys.exit()
def check_noc(j):
    for i in range(3):
        j = input("Enter the number of children : ")
        if j.isdigit():
            noc = j
            return noc
        else:
            print("Please Enter a number\nYou are left with", (3 - (i + 1)), "Attempts.")
    print("Please Try Again Later")
    sys.exit()
def replace_file(file):
    with open(file_name, "w") as primary_file:
        for i in file:
            primary_file.write(i)
def max_salary():
    x = 0
    lines = open(file_name, "r").readlines()
    lines.remove(lines[0])
    for fields in lines:
        fields = fields.split(',')
        Basic = int(fields[2])
        Da = int(fields[3])
        Ma = int(fields[5])
        Salary = Basic + Da + Ma
        # ****Compensation based on Gender******
        if fields[4] == "F":
            Salary = Salary + 200
        # ***Compensation based on Number of children****
        if int(fields[6]) == 0:
            Salary = Salary + 500
        if int(fields[6]) == 1:
            Salary = Salary + 400
        if int(fields[6]) >= 3:
            Salary = Salary - 500
        if Salary > x:
            x, y = round(Salary, 2), fields[1]
    print("Total Salary of", y, "=", x, "is the Max Salary")
def min_salary():
    x = 0
    m = 0
    lines = open(file_name, "r").readlines()
    lines.remove(lines[0])
    for fields in lines:
        fields = fields.split(',')
        Basic = int(fields[2])
        Da = int(fields[3])
        Ma = int(fields[5])
        Salary = Basic + Da + Ma
        # ****Compensation based on Gender******
        if fields[4] == "f":
            Salary = Salary + 200
        # ***Compensation based on Number of children****
        if int(fields[6]) == 0:
            Salary = Salary + 500
        if int(fields[6]) == 1:
            Salary = Salary + 400
        if int(fields[6]) >= 3:
            Salary = Salary - 500
        m = m + 1
        if m == 1:
            x = Salary
        if Salary < x:
            x, y = round(Salary, 2), fields[1]
    print("Total Salary of", y, "=", x, "is the Min Salary")
def sum_salary():
    Salary_of_All_Employees = 0
    lines = open(file_name, "r").readlines()
    lines.remove(lines[0])
    for fields in lines:
        fields = fields.split(',')
        Basic = int(fields[2])
        Da = int(fields[3])
        Ma = int(fields[5])
        Salary = Basic + Da + Ma
        # ****Compensation based on Gender******
        if fields[4] == "f":
            Salary = Salary + 200
        # ***Compensation based on Number of children****
        if int(fields[6]) == 0:
            Salary = Salary + 500
        elif int(fields[6]) == 1:
            Salary = Salary + 400
        elif int(fields[6]) >= 3:
            Salary = Salary - 500
        Salary_of_All_Employees = Salary_of_All_Employees + Salary
    print("Sum oF Everyone's Salary = ", round(Salary_of_All_Employees, 2))
def avg_salary():
    Salary_of_All_Employees = 0
    lines = open(file_name, "r").readlines()
    lines.remove(lines[0])
    m = 0
    for fields in lines:
        m = m + 1
        fields = fields.split(',')
        Basic = int(fields[2])
        Da = int(fields[3])
        Ma = int(fields[5])
        Salary = int(fields[2]) + int(fields[3]) + int(fields[5])
        # ****Compensation based on Gender******
        if fields[4] == "f":
            Salary = Salary + 200
        # ***Compensation based on Number of children****
        if int(fields[6]) == 0:
            Salary = Salary + 500
        if int(fields[6]) == 1:
            Salary = Salary + 400
        if int(fields[6]) >= 3:
            Salary = Salary - 500
        Salary_of_All_Employees = Salary_of_All_Employees + Salary
        Average = Salary_of_All_Employees / m
    print("Average oF Everyone's Salary = ", round(Average, 2))
def insert_data():
    n = int(input("Number of Records: "))
    for i in range(n):
        emp_id = ''
        emp_id_check = get_intgr(emp_id)
        name = ''
        name_check = check_name(name)
        basic = ''
        basic_check = check_basic(basic)
        da = ''
        da_check = check_da(da)
        gender = ''
        gender_check = check_gender(gender)
        noc = ''
        noc_check = check_noc(noc)
        records = [emp_id_check, name_check, basic_check, da_check, gender_check, noc_check]
    p = ''
    for j in range(len(records)):
        p = p + (str(records[j]))
        if j < len(records) - 1:
            p = p + (",")
    row = int(input("Enter the row Where you want to insert this data: "))
    l = 0
    contents = open(file_name, 'r+').readlines()
    with open("fayiq1.csv", 'w') as output_file:
        for i in range(len(contents)):
            l = l + 1
            if i == row:
                output_file.write(p + '\n')
                output_file.write(contents[i])
                for j in range(i + 1, len(contents)):
                    output_file.write(contents[j])
                break

            else:
                if l >= len(contents):
                    output_file.write(p + '\n')
                else:
                    output_file.write(contents[i])
    z = open("fayiq1.csv", "r").readlines()
    replace_file(z)
def sort_file():
    contents = open(file_name, "r").readlines()
    header_line = contents.pop(0)
    with open("fayiq1.csv", "w+") as output_file:
        output_file.write(header_line)
        y = str(input("Sort By Emp_id(e) or Name(n) :"))
        if y == 'e':
            for i in range(len(contents)):
                line = contents[i].split(",")
                for j in range(i, len(contents)):
                    row = contents[j].split(",")
                    if int(line[0]) > int(row[0]):
                        header_line, y = line[0], contents[i]
                        line[0], contents[i] = row[0], contents[j]
                        row[0], contents[j] = header_line, y
                output_file.write(contents[i])
        if y == 'n':
            for i in range(len(contents)):
                line = contents[i].split(",")
                for j in range(i, len(contents)):
                    row = contents[j].split(",")
                    if str(line[1]) > str(row[1]):
                        header_line, y = line[1], contents[i]
                        line[1], contents[i] = row[1], contents[j]
                        row[1], contents[j] = header_line, y
                output_file.write(contents[i])
    z = open("fayiq1.csv", "r").readlines()
    replace_file(z)
def merge_files():
    contents_first = open(file_name, "r")
    contents_first = contents_first.readlines()
    x = contents_first.pop(0)
    y = str(input("Enter the File Name that You want To Merge " + file_name + " with :"))
    y = str(y + '.csv')
    contents_data = open(y, "r")
    contents_data = contents_data.readlines()
    contents_data.pop(0)
    with open("fayiq1.csv", "w")as output_file:
        output_file.write(x)
        for line11 in contents_first:
            output_file.write(line11)
        for line21 in contents_data:
            line22 = line21.split(",")
            x = 0
            for line11 in contents_first:
                line12 = line11.split(",")
                if line22[0] == line12[0]:
                    x = x + 1
            if x == 0:
                output_file.write(line21)
    z = open("fayiq1.csv", "r").readlines()
    replace_file(z)
def update_data():
    n = int(input("Number of Records: "))
    for i in range(n):
        emp_id = ''
        emp_id_check = get_intgr(emp_id)
        name = ''
        name_check = check_name(name)
        basic = ''
        basic_check = check_basic(basic)
        da = ''
        da_check = check_da(da)
        gender = ''
        gender_check = check_gender(gender)
        noc = ''
        noc_check = check_noc(noc)
    records = [emp_id_check, name_check, basic_check, da_check, gender_check, noc_check]
    p = ''
    for j in range(len(records)):
        p = p + (str(records[j]))
        if j < len(records) - 1:
            p = p + (",")
    b = 0
    c = 0
    contents = open(file_name, 'r+').readlines()
    header = contents.pop(0)
    with open("fayiq1.csv", 'w') as output_file:
        y = str(input("Update By Emp_id(e) or Name(n) :"))
        output_file.write(header)
        if y == 'e':
            search_emp_id = int(input("Enter The Emp_Id of the Employee That Is To Be Replaced "))
            for i in range(len(contents)):
                content = contents[i].split(",")
                if search_emp_id == int(content[0]):
                    b = b + 1
            if b == 1:
                for i in range(len(contents)):
                    content = contents[i].split(",")
                    if search_emp_id == int(content[0]):
                        output_file.write(p + '\n')
                    else:
                        output_file.write(contents[i])
            else:
                print("We Found No Records Corresponding to the Emp_Id", search_emp_id, "\nTry Another Emp_Id")
        if y == 'n':
            search_name = str(input("Enter The Name of the Employee That Is To Be Replaced "))
            for i in range(len(contents)):
                content = contents[i].split(",")
                if search_name == str(content[1]):
                    c = c + 1
            if c > 0:
                for i in range(len(contents)):
                    content = contents[i].split(",")
                    if search_name == str(content[1]):
                        output_file.write(p + '\n')
                    else:
                        output_file.write(contents[i])
            else:
                print("We Found No Records Corresponding to the Name", search_name, "\nTry Another Name")
    z = open("fayiq1.csv", "r+").readlines()
    replace_file(z)
def get_intg(u):
    f = list(u)
    for i in f:
        if i.isdigit():
            continue
        else:
            print("invalid Input")
            print("Please Enter again")
            return (f)
def read_int(prompt):
    return int(input(prompt))
def record_data(file):
    con = open(file_name, "a")
    n = int(input("Number of Records: "))
    for i in range(n):
        e = input("Enter the Emp_Id: ")
        # f = read_int(e)
        n = input("Enter The Name of the employee: ")
        b = float(input("Enter " + n + "'s Basic Salary: "))
        d = float(input("Enter DA of " + n + " : "))
        g = input("What Is " + n + "'s Gender (m/f): ")
        m = float(input("Enter Medical Allowance for " + n + ": "))
        o = input("How many Children Does " + n + " have: ")
        records = [e, n, b, d, g, m, o]
        for j in range(len(records)):
            con.write(str(records[j]))
            if j < len(records) - 1:
                con.write(",")
        con.write('\n')
def copy_file(file):
    y = open(file_name, "r").readlines()
    x = str(input("Enter a name for the duplicate file: "))
    x = str(x + '.csv')
    file2 = open(x, "w")
    for i in y:
        print(i)
        file2.write(i)
def write_header(file):
    file.write("Emp_Id,Name,Basic,DA,Gender,MA,NOC\n")
    return
def read_all(c):
    y = path.exists(file_name)
    if y == True:
        x = open(c, 'r').readlines()
        for i in x:
            print(i)
    else:
        print("There Is no File With The Name ", file_name)
        z = str(input("Do you wish to create " + file_name + " (y/n): "))
        if z == 'y':
            print("Creating A File For You ...")
            open_file(file_name)
        elif z == 'n':
            print("Then, What would you like to do")
        else:
            print("Invalid Input")
    return
def open_file(file_name):
    x = path.exists(file_name)
    if x == True:
        open(file_name, "r+")
    else:
        print("Creating A File For you")
        content = open(file_name, "w+")
        write_header(content)
    return (file_name)
if __name__ == '__main__':
    x = str(input("Enter The File Name To Which You Want to Carry Out Operations:"))
    file_name = str(x + '.csv')
    open_file(file_name)
    while True:
        choice = str(input(("open(o), Read(r), duplicate(dp), Record_Data(d), Update(u), Merge(m),\n"
                            "Sort(s), Insert(i), Average_Salary(avg), MaxSalary(max), MinSalary(min),\n"
                            "SumAllSalaries(sum): ")))
        if choice == 'o':
            open_file(file_name)
        elif choice == 'r':
            read_all(file_name)
        elif choice == 'dp':
            copy_file(file_name)
        elif choice == 'd':
            record_data(file_name)
        elif choice == 'u':
            update_data()
        elif choice == 'm':
            merge_files()
        elif choice == 's':
            sort_file()
        elif choice == 'i':
            insert_data()
        elif choice == 'avg':
            avg_salary()
        elif choice == 'sum':
            sum_salary()
        elif choice == 'min':
            min_salary()
        elif choice == 'max':
            max_salary()
        elif choice == 'x':
            break
        else:
            print("Invalid Entry\nPlease Try Again")