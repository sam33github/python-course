import reg

print("Welcome to Employee manager !!")

while True:
    print("you can perform the below operations")
    print("1. Register Employee \n2. View Employee \n3. Update Employee\n4. Delete Employee")
    choice=input("Enter your choice[1,2,3,4] : ")
    if choice=="1":
        print('you have chose registration module')
        reg.reg_details()
    elif choice=="2":
        print("you have chose View Employee!!")
        reg.view_details()
    else:
        print("Invalid choice")
    
    close=input('Do you want to continue (y/n)? :')
    if close=="n":
        break
    elif close=="y":
        continue
    else:
        print("Invalid choice! exiting the program ...!")
        exit()

print("Thanks for using the application!!")
        