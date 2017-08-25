import math
numbers=["4","5","9","6"]
def insertion(numbers):
    for i in range (0,len(numbers)-1):
        while numbers[i]>0 and numbers[i]<numbers [i-1]:
            #numbers[i-1]=numbers[i]
            x = numbers<i
            y = numbers>i

            for x in range(0,i):
                if x > i:
                    x = i

            for y in range(0,i):
                if y < i:
                    y = i

print (insertion(numbers))
