import withd as w
import Appointment as a
import rec as r
import remove as re
def show():
     choice = 0
     while choice != 5:
          print("********************************************")
          print("**       HOSPITAL MANAGEMENT SYSTEM       **")
          print("********************************************")
          print("** [1] PATIENT ENTRY                      **")
          print("** [2] APPOINTMENT                        **")
          print("** [3] RECEIPT                            **")
          print("** [4] HISTORY                            **")
          print("** [5] REMOVE PATIENT                     **")
          print("** [6] EXIT                               **")
          print("********************************************")
          print("********************************************")
          choice = input("Enter your choice : ")

          if choice == "1":
               w.patient()
          elif choice == "2":
               a.appointment()
          elif choice == "3":
               r.receipt()
          elif choice == "4":
               pass
          elif choice == "5":
               re.remove()
          elif choice == "6":
               print("THANK YOU...!")
               break
          else:
               print("Invalid choice")
               continue
show()


