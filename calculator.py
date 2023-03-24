import cal_fun

print("  welcome to your calculator!  ")

print("enter a given choice below :")
print("1.square\n2.rectangle\n3.circle\n4.triangle\n5.sphere" )
user=int(input("enter a number :"))

if user==1:
    print("you choose a square!")
    side=float(input("enter a side :"))
    print(cal_fun.square(side))
    
elif user==2:
        print("you choose a rectangle !")
        lenth=float(input("enter a length :"))
        breath=float(input("enter a breath :"))
        print(cal_fun.rectangle(lenth,breath))
        
elif user==3:
        print("you choose a circle !")
        radious=float(input("enter a radious"))
        print(cal_fun.cirle(radious))
        
elif user==4:
        print("you choose a rectangle !")
        breath=float(input("enter a breath :"))
        length=float(input("enter a lengh :"))
        print(cal_fun.triangle(breath,length))
        
elif user==5:
        print("you choose a sphere !")
        volume=float(input("enter a volume :"))
        print(cal_fun.sphere(volume))

else:
    print("invalid values ...") 

