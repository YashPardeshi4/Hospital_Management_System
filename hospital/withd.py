global Pid1
global Pid2
global Pid3
global fName1
global fName2
global fName3
import info as i
def patient():
    patient1 = {"Patient id : ": "0","Patient First Name : ":"","Patient Last Name : ":""}
    patient2 = {"Patient id : ": "0","Patient First Name : ":"","Patient Last Name : ":""}
    patient3 = {"Patient id : ": "0","Patient First Name : ":"","Patient Last Name : ":""}
    global Pid1
    Pid1 = patient1.get("Patient id : ")
    global Pid2
    Pid2 = patient2.get("Patient id : ")
    global Pid3
    Pid3 = patient3.get("Patient id : ")
    global fName1
    fName1 = patient1.get("Patient First Name : ")
    global fName2
    fName2 = patient2.get("Patient First Name : ")
    global fName3
    fName3 = patient3.get("Patient First Name : ")
    global lName1
    lName1 = patient1.get("Patient Last Name : ")
    global lName2
    lName2 = patient2.get("Patient Last Name : ")
    global lName3
    lName3 = patient3.get("Patient Last Name : ")
    if Pid1 == i.p1:
        i.p1 = input("Enter Patient ID : ")
        i.f1 = input("Enter Patient's First Name : ")
        lName1 = input("Enter Patient's Last Name : ")

    elif Pid2 == i.p2:
        i.p2 = input("Enter Patient ID : ")
        i.f2 = input("Enter Patient's First Name : ")
        lName2 = input("Enter Patient's Last Name : ")

    elif Pid3 == i.p3:
        i.p3 = input("Enter Patient ID : ")
        i.f3 = input("Enter Patient's First Name : ")
        lName3 = input("Enter Patient's Last Name : ")

    else :
        print("Sorry...Ward Full")
