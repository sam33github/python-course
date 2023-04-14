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
    print("s_no\tname,\tage\twork\t\tduration")
    s_no=1
    employees=[]
    
    for emp in data["emp_details"]:
       temp_list=[s_no,emp['name'],emp['age'],emp['work']]
       employees.append(temp_list)
       s_no+=1
       print(employees)
       print(tabulate(employees,headers=["s_no","name","age","work"]))      
        
        
        
        
    
    

    
    