#Biggie Size 
def biggie_size(x):
    for i in range(0,len(x),1):
        if x[i]>0:
            x[i]="big"
    return(x)
#biggie_size([-3,-5,3,7,5])

#Count Positives
def count_positives(x):
    counter=0
    for i in range(0,len(x),1):
        if x[i]>0:
            counter=counter+1
    x[len(x)-1]=counter
    return(x)
#count_positives([-2,0,3,5,7])
 
#Sum Total
def sum_total(x):
    sum=0
    for i in range(0,len(x),1):
        sum=sum+x[i]
    return(sum)
#sum_total([-1,2,3,4])

#Average
def average(x):
    sum=0
    avg=0
    for i in range(0,len(x),1):
        sum=sum+x[i]
    avg=sum/len(x)
    print(avg)
#average([1,2,3,4])

#Length
def length(x):
    y=len(x)
    print(y)
#length([1,2,3])

#Minimum
def minimum(x):
    if len(x)==0:
        return False
    else:
        min=x[0]
        for i in range(0,len(x),1):
            if x[i]<min:
                min=x[i]
    print(min)
#minimum([])

#Maximum
def maximum(x):
    if len(x)==0:
        return False
    else:
        max=x[0]
        for i in range(0,len(x),1):
            if x[i]>max:
                max=x[i]
    print(max)
#maximum([1,3,6,46,7])

#Ultimate Analysis
def ultimate_analysis(list):
    sum=0
    avg=0
    min=list[0]
    max=list[0]
    length=len(list)
    for i in range(0,len(list),1):
        sum=sum+list[i]
        avg=sum/length
        if list[i]>max:
            max=list[i]
        if list[i]<min:
            min=list[i]
    data= {
        'sumTotal':sum,
        'average':avg,
        'minimum':min,
        'maximum':max,
        'length':length
        }
    return(data)
#ultimate_analysis([37,2,1,-9])

#Reverse List
def reverse_list(list):
    x=int(len(list)/2)
    for i in range(x):
        temp=list[i]
        list[i]=list[len(list)-1-i]
        list[len(list)-1-i]=temp
    return(list)
#reverse_list([37,2,1,-9])       

#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

