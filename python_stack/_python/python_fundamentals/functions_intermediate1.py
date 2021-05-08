import random
def randInt(min=0 , max=100):
    if min>max or max<0:
        print("wrong values")
    else:
        num=random.random() * (max-min) + min
        num=round(num)
        print(num)
randInt(min=30,max=20)