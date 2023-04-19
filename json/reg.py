import json
from tabulate import tabulate

def reg_details():
    name=input("enter a name : ")
    age=input("enter a age : ")
    work=input("enter a work : ")
    duration=input("enter a duration : ")
    temp_dict={
        "name":name,
        "age":age,
        "work":work,
        "duration":duration
        }
    with open("file1.json","r")as f :
        data=json.load(f)
    data['emp_details'].append(temp_dict)
    with open("file1.json","w")as f :
        json.dump(data,f,indent=3)
        print("Employee registered successfull!!")


def view_details():
    with open("file1.json","r")as f :
        data=json.load(f)
    s_no=1
    employees=[]
    
    for emp in data["emp_details"]:
       temp_list=[s_no,emp['name'],emp['age'],emp['work']]
       employees.append(temp_list)
       s_no+=1
    print(tabulate(employees,headers=["s_no","name","age","work"]))  


def update_details():
    view_details()
    with open("file1.json","r")as f :
        data=json.load(f)
        sno=1
        choice=input("choose a update details in given no: ")
    for emp in data ["emp_details"]:
        if str(sno)== choice:
            print("what do u like to update :")
            choice2=input("enter your choice :")
            if choice2=="1":
                name=input("enter a name :")
                emp["name"]=name
                print(str(name) + " updated succesfully !!")
                
            elif choice2=="2":
                age=input("enter a age :")
                emp["age"]=age
                print(str(age)+ "updated succesfullty !!")
                
            elif choice2=="3":
                work=input("enter a work :")
                emp["work"]=work
                print(str(work)+ "updated succesfully !!")
                
            elif choice=="4":
                duration=input("enter a duration :")
                print(str[duration]+ "updated succesfully !!")
                
            elif choice=="5":
                name=input("enter a name :")
                age=input("enter a age :")
                work=input("enter a work :")
                duration=input("enter a duration :")
                print("details update sucesssfully")
                
            else:
                ("update invalid")
                break
        sno+=1
    
    with open("file1.json","w")as f :
        json.dump(data,f,indent=3)        
                
                
                
def delete_details():
     view_details()
     with open("file1.json","r")as f :
        data=json.load(f)
        sno=1
        choice=input("choose a delete numbers in given no: ")
     for emp in data ["emp_details"]:
         if str(sno)==choice:
            data["emp_details"].remove(emp)
            print("employee details removed successfully!!")
         sno+=1                    
     with open("file1.json","w")as f :
        json.dump(data,f,indent=3)      
        


        
        
        
        
    
    

    
    