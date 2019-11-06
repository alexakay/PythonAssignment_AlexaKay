import math #this is so that the square root function can be used in task number 5
print(" ") #this is just for looks when it is printed, makes a blank line before the start of my code
print("The speed limit in this area is 50km/hr.\n")
speed = int(input("Please indicate how fast your vehicle was going:"))
if speed >= 51 and speed <= 70: #the code below only applies if the user says they were going somewhere in between 51 and 70
    print("You were going between 1 and 20 miles over the speed limit. You are being fined $45.\n")
elif speed >= 70 and speed <= 80: #the code below only applies if the user says they were going between 71 and 80
    print("You were going between 21 and 30 miles over the speed limit. You are being fined $75.\n")
elif speed >= 80: #the code below only applies if the user says they were going 81 or faster
    print("You were going more than 31 miles over the speed limit. You are being fined $150.\n")
elif speed <= 35: #code below only applies if user says they were going less than 35
    print("You are staying under the speed limit but you are going a bit too slow. Speed up a little bit.\n")
else: #code below only applies if the user says they were going between 36 and 50
    print("Thank you for going the appropriate speed.\n")

win = 0 #win count starts at 0
for x in range (1,7): #asks about win/loss 6 times because there were 6 games
    result = input("W or L in game " + str(x) + "?") #x goes up by 1 each time, so I didn't have to write 6 different print lines saying "game 1", "game 2", etc
    if result == "W" or result == "w":
         win = win + 1 #if the user inputs a win, the win count goes up by 1
if win >= 5: #code below applies if users win count is greater than or equal to 5
    print("You are in group 1 with " + str(win) + " wins\n")
elif win == 3 or win == 4: #code below applies if user won either 3 or 4 games
    print("You are in group 2 with " + str(win) + " wins\n")
elif win ==1 or win == 2: #code below applies if user won 1 or 2 games
    print("You are in group 3 with " + str(win) + " wins\n")
else: #code below applies if user did not win any of their games
    print("You are eliminated due to 0 wins\n")

running1 = 0   #this and the line below allow the code to be looped until "running1" changes to something other than 0
while running1 == 0:
    num_courses = int(input("How many courses did you take this year?"))
    if num_courses > 8: #if user says they took more than 8 courses, it tells them that that's not possible and asks them again for the number of courses that they took this year
        print("You can't take more than 8 courses")
        running1 = 0 #"running1" is still 0 so it asks again how many courses they took
    elif num_courses < 5:
        print("You have to take at least 5 courses")
        running1 = 0  #"running1" is still 0 so it asks again how many courses they took
    if num_courses == 5:
        running1 = 1 #user inputted a number of courses that is possible to have, so "running1" changes to 1 to stop the loop to prevent the computer from asking again how many courses they took
        course1 = int(input("What was your mark in course 1?"))
        course2 = int(input("What was your mark in course 2?"))
        course3 = int(input("What was your mark in course 3?"))
        course4 = int(input("What was your mark in course 4?"))
        course5 = int(input("What was your mark in course 5?"))
        ov_av = (course1 + course2 + course3 + course4 + course5)/5  #adds up all their course marks and divides by number of courses in order to get their average
        print("Your overall average is " + str(ov_av))
    elif num_courses == 6:
        running1 = 1  #user inputted a number of courses that is possible to have, so "running1" changes to 1 to stop the loop to prevent the computer from asking again how many courses they took
        course1 = int(input("What was your mark in course 1?"))
        course2 = int(input("What was your mark in course 2?"))
        course3 = int(input("What was your mark in course 3?"))
        course4 = int(input("What was your mark in course 4?"))
        course5 = int(input("What was your mark in course 5?"))
        course6 = int(input("What was your mark in course 6?"))
        ov_av = (course1 + course2 + course3 + course4 + course5 + course6)/6  #adds up all their course marks and divides by number of courses in order to get their average
        print("Your overall average is " + str(ov_av) + "%")
    elif num_courses == 7:
        running1 = 1  #user inputted a number of courses that is possible to have, so "running1" changes to 1 to stop the loop to prevent the computer from asking again how many courses they took
        course1 = int(input("What was your mark in course 1?"))
        course2 = int(input("What was your mark in course 2?"))
        course3 = int(input("What was your mark in course 3?"))
        course4 = int(input("What was your mark in course 4?"))
        course5 = int(input("What was your mark in course 5?"))
        course6 = int(input("What was your mark in course 6?"))
        course7 = int(input("What was your mark in course 7?"))
        ov_av = (course1 + course2 + course3 + course4 + course5 + course6 + course7)/7  #adds up all their course marks and divides by number of courses in order to get their average
        print("Your overall average is " + str(ov_av))
    elif num_courses == 8:
        running1 = 1  #user inputted a number of courses that is possible to have, so "running1" changes to 1 to stop the loop to prevent the computer from asking again how many courses they took
        course1 = int(input("What was your mark in course 1?"))
        course2 = int(input("What was your mark in course 2?"))
        course3 = int(input("What was your mark in course 3?"))
        course4 = int(input("What was your mark in course 4?"))
        course5 = int(input("What was your mark in course 5?"))
        course6 = int(input("What was your mark in course 6?"))
        course7 = int(input("What was your mark in course 7?"))
        course8 = int(input("What was your mark in course8?"))
        ov_av = (course1 + course2 + course3 + course4 + course5 + course6 + course7 + course8)/8   #adds up all their course marks and divides by number of courses in order to get their average
        print("Your overall average is " + str(ov_av))
if ov_av >= 79.5:  #if their average is greater than or equal to 79.5% then they get the Principal's Award
    print("Congratulations! You have received the Principal's Award for having a 79.5% average or above!\n")

running2 = 0
while running2 == 0: #this line and the line above create a loops that ends when "running2" is equal to something other than 0
    cookies = int(input("How many cookies are produced? You must produce at least 200."))  #asks user how many cookies are produced while running2 = 0
    if cookies < 200:
        print("The minimum is 200 cookies.")
        running2 = 0 #if the number of cookies produced is less than 200, running2 is still equal to 0, therefore the progream asks how many cookies are produced again, it will do this until a number over 199 is entered
    elif cookies > 199:
        running2 = 1 #when a number greater than 199 is entered, running2 changes to something other than 0 (1), therefore ending the loop
crates = int(cookies/(12*20))
cookies = cookies - 12*20*crates
boxes = int(cookies/12)
cookies = cookies - 12*boxes
s_cookie = cookies
cost = (boxes*5)+(crates*80)+(s_cookie*5)
if crates == 1:   #if only 1 crate is produced, the program says "is"
    print("There is " + str(crates) + " crate being produced.")
else: #if 0 or more than 1 crate is produced, the program says "are"
    print("There are " + str(crates) + " crates being produced.")
if boxes == 1:  #if only 1 box is produced, the program says "is"
    print("There is " + str(boxes) + " box being produced.")
else:  #if 0 or more than 1 box  is produced, the program says "are"
    print("There are " + str(boxes) + " boxes being produced.")
if s_cookie == 1: #if only 1 single cookie is produced, the program says "is"
    print("There is " + str(s_cookie) + " single cookie remaining.")
else: #if 0 or more than 1 single cookie  is produced, the program says "are"
    print("There are " + str(s_cookie) + " single cookies remaining.")
print("The total cost is $" + str(cost) + ".\n")

running = 0
while running == 0: #this line and the line above create a loops that ends when "running" is equal to something other than 0
    which = input("Which program would you like to run? Quick pythagoras (1), tip calculator (2), or temperature converter (3)?") #asks which task they want, but only when running = 0
    if which != "1" and which != "2" and which != "3":
        print("Please enter either 1, 2, or 3.")
        running = 0 #is user enters something other than 1, 2, or 3, running is still equal to 0, therefore it will ask which task they want again, it will do this until they enter either 1, 2, or 3
    if which == "1":
        running = 1 #they entered 1 (starts a task) so the program doesn't need to ask them again which task they want, and it wont ask them because running no longer equals 0
        hypotenuse = 0 #sets hypotenuse to 0
        for x in range (0,2): #asks the question below two times
            pyth_inp = int(input("What is one of your two side lengths?"))
            hypotenuse = (pyth_inp * pyth_inp + hypotenuse) #multiplies one of the side lengths, squared, by the other, squared, and adds the hypotenuse (which is 0)
        hypotenuse = math.sqrt(hypotenuse) #square roots the hypotenuse
        print("Your hypotenuse = " + str(round(hypotenuse,2)) + "\n") #prints hypotenuse and rounds it to two decimal places
        repeat1 = input("Would you like to repeat this program (1)? Or end here (2)?") #asks if they would like to repeat the program or end
        if repeat1 != "1" and repeat1 != "2":
            print("Please enter either 1 or 2.")
            repeat1 = input("Would you like to repeat this program (1)? Or end here (2)?") #asks again if user entered something other than 1 or 2
        elif repeat1 == "1":
            running = 0  #asks which program they would like to run, as running now equals 0 again
        elif repeat1 == "2":
            print("Thank you for using the program.")
            running = 1 #they chose to end the program, so running now equals something other than 0 so that it wont ask the question again of which program they would like to run
    elif which == "2":
        running = 1 #they entered 1 (starts a task) so the program doesn't need to ask them again which task they want, and it wont ask them because running no longer equals 0
        bill = int(input("What was your total on the bill?"))
        tip = int(input("What is the tip percentage?"))
        total = ((bill*(tip/100)) + bill) #tip/100 turns the tip as a whole number into a decimal, multiply the bill amount by the decimal tip to get the tip amount, and then add bill amount to get the total bill charge
        print("Your total is $" + str(round(total,2)) + "\n")
        repeat2 = input("Would you like to repeat this program (1)? Or end here (2)?") #asks if they would like to repeat the program or end
        if repeat2 != "1" and repeat2 != "2":
            print("Please enter either 1 or 2.")
            repeat2 = input("Would you like to repeat this program (1)? Or end here (2)?") #asks again if user entered something other than 1 or 2
        elif repeat2 == "1":
           running = 0 #asks which program they would like to run, as running now equals 0 again
        elif repeat2 == "2":
            print("Thank you for using the program.")
            running = 1 #they chose to end the program, so running now equals something other than 0 so that it wont ask the question again of which program they would like to run
    elif which == "3":
        running = 1 #they entered 1 (starts a task) so the program doesn't need to ask them again which task they want, and it wont ask them because running no longer equals 0
        fc = input("Is your temperature in fahrenheit (1) or celsius (2)?")
        if fc != "2" and fc != "1":
            print("Please enter either 1 or 2")
            fc = input("Is your temperature in fahrenheit (1) or celsius (2)?") #asks again if user entered something other than 1 or 2
        if fc == "1":
            tempf = int(input("What is your fahrenheit temperature?"))
            tempfc = (((tempf-32)*5)/9)  #formulq for converting fahrenheit to celsius
            print(("Your fahrenheit temperature, " + str(round(tempf,1)) + "ºF, is " + str(round(tempfc,1)) + "ºC in celsius\n")) #prints the converted temperature, rounded to one decimal place
            repeat3 = input("Would you like to repeat this program (1)? Or end here (2)?") #asks if they would like to repeat the program or end
        elif fc == "2":
            tempc = int(input("What is your celsius temperature?"))
            tempcf = (tempc * 1.8) + 32 #formule for converting celsius to fahrenheit
            print("Your celsius temperature, " + str(round(tempc,1)) + "ºC, is " + str(round(tempcf,1)) + "ºF in fahrenheit\n")  #prints the converted temperature, rounded to one decimal place
            repeat3 = input("Would you like to repeat this program (1)? Or end here (2)?") #asks if they would like to repeat the program or end
        if repeat3 != "1" and repeat3 != "2":
            print("Please enter either 1 or 2.")
            repeat3 = input("Would you like to repeat this program (1)? Or end here (2)?") #asks again if user entered something other than 1 or 2
        if repeat3 == "1":
            running = 0 #asks which program they would like to run, as running now equals 0 again
        elif repeat3 == "2":
            print("Thank you for using the program.")
            running = 1   #they chose to end the program, so running now equals something other than 0 so that it wont ask the question again of which program they would like to run