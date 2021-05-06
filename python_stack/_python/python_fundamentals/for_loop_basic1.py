#Basic
for x in range(0,150,1):
    print(x)
#Multiples of Five
for x in range(5,1000,5):
    print(x)
#Counting, the Dojo Way
for x in range(1,100,1):
    if x%10==0:
       print("Coding")
    elif x%5==0:
       print("Coding Dojo")
#Whoa. That Sucker's Huge
sum=0
for x in range(0,500000,1):
    if x%2==1:
       sum=sum+x
print(sum)
#Countdown by Fours
for x in range(2018,0,-4):
   print(x)
#Flexible Counter 
lowNum=0
highNum=16
mult=2
for x in range(lowNum,highNum,1):
    if x%mult==0:
        print(x)

