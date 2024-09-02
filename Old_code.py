from random import choice
from time import sleep

answered, correct, mode, r, y = 0, 0, '', 0, 0

def difficulty():
    global r, y, mode
    
    d = input("""Select a mode by typing a number:
1. 1x1
2. 1x2
3. 1x3
4. 2x2
5. 3x2
6. 3x3
Press the enter key at any time to quit
""")

    
    if d == '1':
        mode = '1x1'
        r = list(range(1,10))
        y = list(range(1,10))
        ask()
    
    elif d == '2':
        mode = '1x2'
        r = list(range(1,10))
        y = list(range(1,100))
        ask()

    elif d == '3':
        mode = '1x3'
        r = list(range(1,10))
        y = list(range(1,1000))
        ask()
    
    elif d == '4':
        mode = '2x2'
        r = list(range(1,100))
        y = list(range(1,100))
        ask()

    elif d == '5':
        mode = '2x3'
        r = list(range(1,100))
        y = list(range(1,1000))
        ask()
    
    elif d == '6':
        mode = '3x3'
        r = list(range(1,1000))
        y = list(range(1,1000))
        ask()

    elif d == 'd':
        print("\nPick a difficulty first silly!\n")
        sleep(2)
        difficulty()

    elif d == '':
        exit()

    else:
        print('Invalid input')
        difficulty()

def ask():
    global answered, correct

    a = int(choice(r))
    b = int(choice(y))
    quest = input(f"{a} x {b}= ")
    ans = a * b

    try:
        if int(quest) == ans:
            print ('Correct!')
            answered += 1
            correct += 1
            ask()
        
        else:
            print(f"Wrong! The answer is {ans}")
            answered += 1
            ask()
            
    except ValueError:
        if quest.lower() == 'stats':
            print(f"Mode: {mode}\n"
            f"Answered: {answered}\n"
            f"Correct answers: {correct}\n"
            f"% accuracy: {round((correct/answered)*100, 2)}\n")
            ask()

        elif quest == '':
            print(f"Mode: {mode}\n"
            f"Answered: {answered}\n"
            f"Correct answers: {correct}\n"
            f"% accuracy: {round((correct/answered)*100, 2)}\n")     
            sleep(5)
            exit()

        elif quest == 'd':
            print(f"Mode: {mode}\n"
            f"Answered: {answered}\n"
            f"Correct answers: {correct}\n"
            f"% accuracy: {round((correct/answered)*100, 2)}\n")
            sleep(2)            
            answered, correct = 0, 0
            difficulty()      
    
        else:
            q = input(f"press enter to continue or type exit"
            f" to quit\n")
        
            if q.lower() == 'exit':
                print(f"Mode: {mode}"
                f"Answered: {answered}"
                f"Correct answers: {correct}"
                f"% accuracy: {round((correct/answered)*100, 2)}\n")
                sleep(5)
                exit()

            elif q.lower() == '':
                ask()

difficulty()