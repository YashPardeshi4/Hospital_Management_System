import info as i
def diabetes1():
    print("********************************************")
    print("**             Dr. Salman Khan            **")
    print("********************************************")
    app = input("Do you want to confirm your appointment [Y/N] :")
    if app == "Y" or app == "y":
        i.day1 = input("Please Enter Date (DD/MM/YYYY) : ")
        i.time1 = input("Please Enter time : ")
        print("THANK YOU...")
    elif app == "N" or app == "n":
        print("Thank You..")
    else:
        print("Invalid Choice")

def diabetes2():
    print("********************************************")
    print("**             Dr. Salman Khan            **")
    print("********************************************")
    app = input("Do you want to confirm your appointment [Y/N] :")
    if app == "Y" or app == "y":
        i.day2 = input("Please Enter Date (DD/MM/YYYY) : ")
        i.time2 = input("Please Enter time : ")
        print("THANK YOU...")

    elif app == "N" or app == "n":
        print("Thank You..")
    else:
        print("INVALID CHOICE...")

def diabetes3():
    print("********************************************")
    print("**             Dr. Salman Khan            **")
    print("********************************************")
    app = input("Do you want to confirm your appointment [Y/N] :")
    if app == "Y" or app == "y":
        i.day3 = input("Please Enter Date (DD/MM/YYYY) : ")
        i.time3 = input("Please Enter time : ")
        print("THANK YOU...")

    elif app == "N" or app == "n":
        print("Thank You..")
    else:
        print("INVALID CHOICE...")