import json

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


def view_emp():
    with open("file1.json","r")as f :
        data=json.load(f)
    print("s.no\tname\t\tage\twork\t\tduration ")
    s_no=1
    c_manager=0
    for emp in data['emp_details']:
        if emp["work"]=="Manager":
            c_manager+=1
        print(f"{str(s_no)}\t{emp['name']}\t\t{emp['age']}\t{emp['work']}\t\t{emp['duration']}")
        s_no+=1
    print("No. of managers : " + str(c_manager))