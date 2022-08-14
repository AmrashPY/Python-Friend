import easygui
import os
import time
import pyfiglet
from termcolor import colored, cprint





out = pyfiglet.figlet_format("Amrash")
print(out)
print("Greetings friend!")
time.sleep(1)
name = input("What is your name?: ")
time.sleep(1)
print("Hello " + name)
time.sleep(1)


age = input("How old are you?: ")
print("Oh, " + age)
time.sleep(1)
print("Cool, im your digital friend!")
time.sleep(2)

hunger = input("Are you hungry?: ")
if hunger == "yes":
    time.sleep(2)
    print("Go get some food, and dont forget to come back!") 
    time.sleep(5)

else:
    print("Thats awesome, then you can stay here with me!")
    time.sleep(3)

print("Oh no i spoke to soon, I think our time here has come to an end!: ")
time.sleep(3)
print("The world is collapsing!")
time.sleep(5)

input("Thank you for visiting my program, press enter to close.")







