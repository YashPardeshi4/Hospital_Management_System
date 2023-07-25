import info as i
import diabetes as d
import cancer as c
import bloodPres as b
import heart as h

def appointment():
    choice = 0
    while choice != "6":
        print("********************************************")
        print("**             CHOOSE DISEASE             **")
        print("********************************************")
        print("** [1] DIABETES                           **")
        print("** [2] CANCER                             **")
        print("** [3] BLOOD PRESSURE                     **")
        print("** [4] HEART                              **")
        print("** [5] MAIN MENU                          **")
        print("********************************************")
        print("********************************************")
        choice = input("Enter your choice : ")
        if choice == "1":
            pid=input("Enter Your Patient ID : ")

            if pid == i.p1:
                d.diabetes1()
            elif pid == i.p2:
                d.diabetes2()
            elif pid == i.p3:
                d.diabetes3()

        elif choice == "2":
            pid=input("Enter Your Patient ID : ")

            if pid == i.a:
                c.cancer1()
            elif pid == i.b:
                c.cancer()
            elif pid == i.e:
                c.cancer()

        elif choice == "3":
            pid = input("Enter Your Patient ID : ")

            if pid == i.a:
                b.blood_pressure()
            elif pid == i.b:
                b.blood_pressure()
            elif pid == i.e:
                b.blood_pressure()

        elif choice == "4":
            pid = input("Enter Your Patient ID : ")

            if pid == i.a:
                h.heart()
            elif pid == i.b:
                h.heart()
            elif pid == i.e:
                h.heart()

        elif choice == "5":
            break
        else:
            print("Invalid choice...")
            continue
