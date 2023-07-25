import info as i
def heart1():
    print("********************************************")
    print("**             Dr.Akshay Kumar            **")
    print("********************************************")
    app = input("Do you want to confirm your appointment [Y/N] :")
    if app == "Y" or app == "y":
        i.day1 = input("Please Enter Date (DD/MM/YYYY) : ")
        i.time1 = input("Please Enter time : ")
        print("THANK YOU...")

    elif app == "N" or app == "n":
        print("Thank You..")
    else:
        print("INVALID CHOICE...")