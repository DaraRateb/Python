#Countdown
def countdown(x):
    for x in range(x,0,-1):
        return(x)
#countdown(5)

#Print and Return
def print_and_return(x):
    print(x[0])
    return(x[1])
#print_and_return([80,2])

#First Plus Length
def first_plus_legth(x):
    sum=x[0]+len(x)
    return(sum)
#first_plus_legth([1,2,3,4,5])

#Values Greater than Second 
def new_list(x):
    if len(x)<2:
        return False
    else:
        counter=0
        y = []
        for i in range (0,len(x),1):
            if x[i]>x[2]:
                counter=counter+1
                y.append(x[i])
    print(counter)
    return(y)   
#new_list([5,2,3,4])

#This Length, That Value
def length_and_value(s,v):
    y=[]
    y=[v]*s
    return(y)
#length_and_value(5,2)

    


