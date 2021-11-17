from random import randint as rn
import time

def addition(num1,num2):
    return num1 + num2
def subtraction(num1,num2):
    return num1 - num2
def multiplication(num1,num2):
    return num1 * num2
def devision(num1,num2,roundInt=3):
    return round((num1 / num2),roundInt)
def increment(num):
    return num + 1
def decrement(num):
    return num - 1


for i in range(3):
    num1 = rn(1,10000);num2 = rn(1,10000)#generate the used numbers to demonstrate funsctions
    print(f'Used numbers {num1} & {num2}')
    print(f'{num1} + {num2} = {addition(num1,num2)}')
    print(f'{num1} - {num2} = {subtraction(num1,num2)}')
    print(f'{num1} * {num2} = {multiplication(num1,num2)}')
    print(f'{num1} / {num2} = {devision(num1,num2)}')
    print(f'{num1} + 1 = {increment(num1)}')
    print(f'{num1} - 1 = {decrement(num1)}\n\n')
    time.sleep(2.5)
