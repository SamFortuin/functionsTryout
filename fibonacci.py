from typing import Sequence


num1 = 0
num2 = 1
num3 = 1
fibList = []
def fibonacci(howMany,sequence):
    for i in range(howMany):
        global num1 ; global num2 ; global num3
        num3 = num1 + num2
        fibList.append(num3)
        num1 = num2
        num2 = num3
    if sequence == 'single':
        return fibList[howMany-1]
    elif sequence == 'sequence':
        return fibList

#sequence print looks kinda weird but it works, change second arg to 'sequence'
where = int(input('Which spot in the sequence would you like to see?\n'))
print('Spot',where,'in the fibonacci chain is',str(fibonacci(where,'single')).replace('[','').replace(']',''))
