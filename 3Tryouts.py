def name():
    name = input("What is your name?\n")
    return name

def age():
    age = input('How old are you?\n')
    return age

def nameAge():
    while True:
        print(f'Your name is {name()} and you are {age()} years old.')
        loopAsk = input('do you want to continue\n').lower()
        if loopAsk == 'y' or loopAsk == 'yes':
            pass
        elif loopAsk == 'n' or loopAsk == 'no':
            break
        else:
            print('Invalid input')
            break

nameAge()