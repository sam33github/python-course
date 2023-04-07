
# i=10
# while i>0:

#     print(i) 
#     i-=1
    
    
give_values=['abc','xyz','aaa','accc','14521']
len_values=len(give_values)
i=0
num=0
while   i<len_values:
    if  len(give_values[i])>=2 and give_values[i][0]==give_values[i][-1]:
        num+=1
    i=i+1
print(num)
        
    