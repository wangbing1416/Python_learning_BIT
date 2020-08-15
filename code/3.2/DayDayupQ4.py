def dayUP(df):
    dayup=1
    for i in range(365):
        if i%7 in[6,0]:
            dayup*=(1-0.01)
        else:
            dayup*=(1+dayfactor)
    #print("工作日的力量为{:.2f}".format(dayup))
    return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:
    dayfactor+=0.001
print("需要工作日努力{:.3f}%".format(dayfactor*100))
