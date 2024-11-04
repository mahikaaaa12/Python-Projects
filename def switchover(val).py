def switchover(val):
    for i in range(0,len(val),2):
        val[i],val[i+1]=val[i+1],val[i]
    return val
val=list(eval(input("Enter a list:")))
print("The modified list is:",switchover(val))
