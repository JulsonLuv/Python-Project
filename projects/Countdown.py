import time

def printer():
    print("░█▀▀▀█░█▀▀▀█░█▀▀▄░█▀▀▀█░█▀▀░█") 
    print("░▀▀▀▄▄░█▄▄▄█░█▀▀▄░█▀▀▀▄░█░░░█")
    print("░█▄▄▄█░█░░░█░█▄▄▀░█▄▄▄█░█▄▄░█")
    ss = '*'* 60
    content= (f'{ss} \n U HAVE BEEN HACKED \n {ss}')
    return content
    
    

def countdown(user_time):
    while user_time >= 0:
        mins, secs = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        user_time -= 1
    print(printer())


if __name__ == '__main__':
    while True:
        user_time = input("Enter a time in seconds: ")
        if user_time.isdigit():
            user_time = int(user_time)
            break
        else:
            print('You MUST use digits!')

    countdown(user_time)
    #user_time = int(input("Enter a time in seconds: "))
    #countdown(user_time)