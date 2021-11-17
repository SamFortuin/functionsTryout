num = input("Van welk getal wilt u de tafel zien?\n")

def numConvert():
    global num
    numConvert = False
    for i in range(10):
        if str(i) in num:
            numConvert = True
    if numConvert == True:
        num = int(num)
    else:
        print('Niet een getal.')
        exit()

def tafel(tafelNum):
    tafelList = []
    i = 1
    while i <= 10:
        tafelList.append(i*tafelNum)
        i += 1
    print(*tafelList,sep=', ')
    

numConvert()
tafel(num)