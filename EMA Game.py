import math
import sys
def main():
    global life
    life = 3
    input("Welcome to the Math Dungeon Game! Press Enter to continue! (Any time a text prompt ends, press enter to continue.)")
    input("You're a young traveller going across the lands to find the sacred fortress when you come across a large mountain, you realize that the mountain is too steep to climb and there is no way around it, however you do see a small opening at the bottom of the mountain that resembles a cave!")
    input("You descend into the cave and find a large wooden door, with a sign on top that reads 'Only those with wisdom may enter, be warned, those without the intellect necessary to pass this mountain will perish by the hand of the curse of the mountain.'")
    input("You figure you are smart enough and open the door to go into the dungeon.")
    room1()
    win()

def death():
    input("You have lost all of your lives and the curse of the mountain consumes you.")
    input("You slowly lose conscienceness until you fade away into death...")
    input("This is the end of the game.")
    replay = input("Would you like to play again? (yes or no)?: ")
    if replay.lower() == "yes":
        main()
    else:
        sys.exit()

def win():
    input("Finally! Fresh air...you've made it out of the dungeon alive...and you feel a little wiser now that you've completed it.")
    input("Thank you for playing.")
    replay = input("Would you like to play again? (yes or no)?: ")
    if replay.lower() == "yes":
        main()
    else:
        sys.exit()

def room11():
    global life
    q1 = input("What is the slope in the derivative of the equation y=5x²+10x-3?: ")
    if q1 == "10":
        input("That is correct.")
    else:
        while q1 != "10":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "10":
                input("That is correct.")
    input("You see the one door open in front of you, and you realise that it's the outside world again!")
    

def room10():
    global life
    q1 = input("What is the value of y in the equation y=cosθ when θ is 0?: ")
    if q1 == "1":
        input("That is correct.")
    else:
        while q1 != "1":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "1":
                input("That is correct.")
    direction = input("You see two doors open up in front of you, do you go left or straight?: ")
    if direction.lower() == "left":
        room9()
    elif direction.lower() == "straight":
        room11()
    else:
        direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "left":
                room9()
                break
            elif direction.lower() == "straight":
                room11()
                break

def room9():
    global life
    q1 = input("A line that is tangent to a circle touches the circle at how many points?: ")
    if q1 == "1":
        input("That is correct.")
    else:
        while q1 != "1":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "1":
                input("That is correct.")
    direction = input("You see three doors open up in front of you, do you go left, straight, or right?: ")
    if direction.lower() == "left":
        room8()
    elif direction.lower() == "straight":
        room11()
    elif direction.lower() == "right":
        room10()
    else:
        direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "left":
                room8()
                break
            elif direction.lower() == "straight":
                room11()
                break
            elif direction.lower() == "right":
                room10()
                break


def room8():
    global life
    q1 = input("What is the value of the tangent of an angle times the cotangent of the same angle?: ")
    if q1 == "1":
        input("That is correct.")
    else:
        while q1 != "1":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "1":
                input("That is correct.")
    direction = input("You see two doors open up in front of you, do you go straight or right?: ")
    if direction.lower() == "straight":
        room11()
    elif direction.lower() == "right":
        room9()
    else:
        direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "straight":
                room11()
                break
            elif direction.lower() == "right":
                room9()
                break



def room7():
    global life
    q1 = input("A triangle has two angles that measure 45 degrees each. What is the measure of the third angle? Do not include 'degrees' in your answer, simply give it's value: ")
    if q1 == "90":
        input("That is correct.")
    else:
        while q1 != "90":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "90":
                input("That is correct.")
    direction = input("You see two doors open up in front of you, do you go left or straight?: ")
    if direction.lower() == "left":
        room6()
    elif direction.lower() == "straight":
        room10()
    else:
        direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "left":
                room6()
                break
            elif direction.lower() == "straight":
                room10()
                break


def room6():
    global life
    q1 = input("How many degrees is a right angle? (Only give the numerical value of the answer, do not include units): ")
    if q1 == "90":
        input("That is correct.")
    else:
        while q1 != "90":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "90":
                input("That is correct.")
    direction = input("You see three doors open up in front of you, do you go left, straight, or right?: ")
    if direction.lower() == "left":
        room5()
    elif direction.lower() == "straight":
        room9()
    elif direction.lower() == "right":
        room7()
    else:
        direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "left":
                room5()
                break
            elif direction.lower() == "straight":
                room9()
                break
            elif direction.lower() == "right":
                room7()
                break


def room5():
    global life
    q1 = input("What is the measure of the angle that is complementary to an angle that is 30 degrees? (Only give the value of the angle, not the word degrees after it.): ")
    if q1 == "30":
        input("That is correct.")
    else:
        while q1 != "60":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "30":
                input("That is correct.")
    direction = input("You see two doors open up in front of you, do you go straight or right?: ")
    if direction.lower() == "straight":
        room8()
    elif direction.lower() == "right":
        room6()
    else:
        direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "straight":
                room8()
                break
            elif direction.lower() == "right":
                room6()
                break


def room4():
    global life
    q1 = input("What is the point of intersection of the two lines y = x and y = -x? (x,y): ")
    if q1 == "(0,0)":
        input("That is correct.")
    else:
        while q1 != "(0,0)":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "(0,0)":
                input("That is correct.")
    direction = input("You see two doors open in front of you, do you go left or straight?: ")
    if direction.lower() == "left":
        room3()
    elif direction.lower() == "straight":
        room7()
    else:
        direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "left":
                room3()
                break
            elif direction.lower() == "straight":
                room7()
                break


def room3():
    global life
    q1 = input("What is the y-intercept of the formula y = 17x + 1?: ")
    if q1 == "1":
        input("That is correct.")
    else:
        while q1 != "1":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "1":
                input("That is correct.")
    direction = input("You see three doors open up in front of you, do you go left, straight, or right?: ")
    if direction.lower() == "left":
        room2()
    elif direction.lower() == "straight":
        room6()
    elif direction.lower() == "right":
        room4()
    else:
        direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "left":
                room2()
                break
            elif direction.lower() == "straight":
                room6()
                break
            elif direction.lower() == "right":
                room4()
                break


def room2():
    global life
    q1 = input("What is the slope of the formula y = 3x + 7?: ")
    if q1 == "3":
        input("That is correct.")
    else:
        while q1 != "3":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "100":
                input("That is correct.")
    direction = input("You see two doors open up in front of you, do you go straight or right?: ")
    if direction.lower() == "straight":
        room5()
    elif direction.lower() == "right":
        room3()
    else:
        direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "straight":
                room5()
                break
            elif direction.lower() == "right":
                room3()
                break



def room1():
    global life
    q1 = input("What is 25 times 4?: ")
    if q1 == "100":
        input("That is correct.")
    else:
        while q1 != "100":
            q1 = input("That is incorrect, you lose a life, try again: ")
            life = life - 1
            if life == 0:
                death()
            if q1 == "100":
                input("That is correct.")
    direction = input("You see three doors open up in front of you, do you go left, straight, or right?: ")
    if direction.lower() == "left":
        room2()
    elif direction.lower() == "straight":
        room3()
    elif direction.lower() == "right":
        room4()
    else:
        while direction.lower() != "left" or direction.lower() != "right" or direction.lower() != "straight":
            direction = input("It doesn't seem you can go that way, please select a direction to go that is available: ")
            if direction.lower() == "left":
                room2()
                break
            elif direction.lower() == "straight":
                room3()
                break
            elif direction.lower() == "right":
                room4()
                break








main()
