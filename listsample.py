samplelist=['aba','xyx','aba','1221']
count=0
if  len(samplelist[0])>=2 and samplelist[0][-1]==samplelist[0][0]  :
        count=count+1
        
if  len(samplelist[1])>=2:

   if   samplelist[1][-1]==samplelist[1][0]:
        count=count+1      
        
if  len(samplelist[2])>=2:

   if   samplelist[2][-1]==samplelist[2][0]:
        count=count+1
        
if  len(samplelist[3])>=2:

   if   samplelist[3][-1]==samplelist[3][0]:
        count=count+1
        
print(count)