import json_file_generator
from json import load
from os import system
from random import randint
from sys import exit
from time import sleep, time

class Question:
    """A multiplication sum to be answered"""

    def __init__(self, left_dim, right_dim):
        """
        The arguments are the number of digits for each number in the problem.
        The class attributes are then randomly assigned numbers that fit the 
        citeria.
        """
        self.left = randint(10**(left_dim-1), 10**(left_dim))
        self.right = randint(10**(right_dim-1), 10**(right_dim))
        self.answer = self.left*self.right

    def ask_and_check(self):
        """
        Displays the question and gets the answer. Bad input handling is done
        within another function where it's called
        """
        global ans
        ans = input(f"{self.left} x {self.right} = ")
        
        return int(ans) == self.answer
        
modes = ["1x1", "1x2", "1x3", "2x2", "2x3", "3x3"]
"""That's a surprise tool that will help us later ;-)"""

def close():
    """
    Closing sequence. Can't leave without saying bye! :)
    """
    system("cls")
    print("Goodbye!\nExiting...")
    sleep(1)
    exit()

def difficulty():
    """
    Prompts user to select what mode they want to play in, or to check their
    lifetime stats in each mode. Calls itself recursively until the user decides
    to quit by pressing enter. 
    """
    selecting = True
    system("cls")
    
    select_str = (f"Select a mode by typing a number:"
                  f"\n1. 1x1 \n2. 1x2 \n3. 1x3 \n4. 2x2 \n5. 2x3 \n6. 3x3\n")
    d = input(select_str+"\n7. Check stats\nPress enter to quit (double press ingame).\n")
        
    try:
        d = int(d)
        if d in range(1,7):
            return modes[d-1] #Oh toodles!!! :-)        
        elif d == 7:
            system("cls")
            try:
                display_stats(modes[int(input(select_str+"\n"))-1])
                    
            except (IndexError, ValueError):
                system("cls")
                print("Invalid!")
                sleep(3)
                play(difficulty())
            
        else:
            system("cls")
            print("Invalid mode selected")
            sleep(3)
            return False
        
    except ValueError:
        if d == "":
            close()
                
        else:
            system("cls")
            print("Invalid mode selected")
            sleep(3)
            return False

def play(mode):
    """
    This play() function always comes in a pair with difficulty(), so the mode
    argument is always with either a valid mode, or False. In the latter case, 
    the if block below tries again until the user does things properly.
    """

    if not mode:
        play(difficulty())

    session_stats = {"Correct": 0,
                     "Answered": 0,
                     "Time": 0}
    
    start = round(time(), 2)
    end = round(time(), 2) #to help log practice time
    asking = True
    
    while asking: 
        """
        Generates and asks instances of the Question class. Also updates current
        session stats. 
        """
        
        system("cls")
        q = Question(int(mode[0]), int(mode[2]))

        try:
            if q.ask_and_check():
                print("Correct!")
                sleep(.5)
                session_stats["Answered"] += 1
                session_stats["Correct"] += 1
                end = round(time(), 2) - .5  #compensation
                continue

            else:
                print("Wrong!")
                sleep(.5)
                session_stats["Answered"] += 1
                end = round(time(), 2) - .5
                continue

        except ValueError:
            if ans == "":
                session_stats["Time"] = end - start
                if session_stats["Answered"] > 0:
                    json_file_generator.update_stats(mode, session_stats)
                asking = False

            else:
                print(f"Invalid input!")
                sleep(0.5)
                session_stats["Answered"] += 1
                end = round(time(), 2) - .5
                continue

        play(difficulty()) 

def display_stats(mode):
    """Self explanatory name; does some calculations and shows stats for the given mode"""

    statfile = f"lifetime_stats\{mode}lifetime_stats.json"
    stats = {}

    system("cls")
    try:
        with open(statfile, "r") as stats_dict:
            stats = load(stats_dict)
            minutes = str(int(stats["Time"])//60).zfill(2) + ":" + str(int(stats["Time"])%60).zfill(2)
            show = (f"Mode: {mode} \nAnswered: {stats['Answered']}\n"
                    f"Accuracy: {round((stats['Correct']/stats['Answered'])*100, 2)}%\n"
                    f"Total time: {minutes}\n"
                    f"Time per question (avg): {round(int(stats['Time'])/stats['Answered'], 2)}s")
            
            idk = input(show) #junk input to keep the show running
            play(difficulty())
    
    except FileNotFoundError:
        print("Maybe try playing that mode first...")
        sleep(3)
        play(difficulty())
        
if __name__ == "__main__":
    system("cls")
    play(difficulty())
