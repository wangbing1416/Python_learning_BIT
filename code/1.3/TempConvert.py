TempStr=input("please input a value of temperate with signal:")
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print("the value after being calculated is {:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F=eval(TempStr[0:-1])*1.8+32
    print("the value after being calculated is {:.2f}F".format(F))
else :
    print("format error!")
