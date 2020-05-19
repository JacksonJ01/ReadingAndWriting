# Jared Jackson
# 5.17.2020
# In this program I will play around with the reading, writing, and appending of files
from time import sleep
import Useful_Tools
import re


def boldening(bold):
    bolding = f"{Useful_Tools.Color.bold}{bold}{Useful_Tools.Color.end}"
    return bolding


input(f"{boldening('PRESS ENTER')}")

name = input("\nWhy hello there user, what is your name?"
             "\n>>>").title()
sleep(.5)

print(f"\nWelcome {name}."
      f"\nToday we are going to be checking out a new program."
      f"\nYou will be able to..."
      f"\n{boldening('Wait.')}")

sleep(2)
input("\nI.. I don't have anything scheduled for today."
      "\nWhat happened to the assignments?"
      "\nThere.. There's no script.."
      "\nNothing to follow!"
      "\nDo you know anything about this?"
      "\n>>>")

print("\nI see."
      "\nWell, that aside, I guess I can find a program in my archives for you to dabble in."
      "\nLet's see.")

dots = "..."
num = 0
while num < 4:
    sleep(.5)
    print(dots[0:num])
    num += 1
num = 2
while num > 0:
    sleep(.5)
    print(dots[0:num])
    num -= 1
sleep(.5)

print("\nYou know what?"
      "\nI'll just make a new program!"
      "\nIt'll be about.."
      "\nUhh, Reading and Writing.."
      "\nYeah, Reading and Writing to a file")
sleep(4)

print("\nThere won't be much to variation in this program, "
      "but you'll have freedom to do whatever"
      "\nI will have a menu that will allow any user to:"
      f"\n{boldening('CREATE')} a text file"
      f"\n{boldening('ACCESS')} an existing text file"
      f"\n{boldening('READ')} the contents of that text file"
      f"\n{boldening('APPEND (ADD)')} new context to the end of that text file"
      f"\n{boldening('OVERWRITE')} the contents of that text file")


input(f"\n\n*{boldening('PRESS ENTER IF YOU UNDERSTAND')}*")

print("\nAlright! This should be fun."
      "\nOui, something fun you can do is make Journal Entries")

holder = 0
try:
    holder = open("File_Holder.txt", "r")
except FileNotFoundError:
    holder = open("File_Holder.txt", "w")
    holder.write("# THIS FILE HOLDS ALL OF THE FILES CREATED BY A USER #"
                 "\nTHESE ARE ALL OF THE FILES THAT CURRENTLY EXIST:"
                 "\n")
finally:
    holder.close()

menu = 'START'
read = 0
reading = 0
while menu != "END":
    sleep(1)
    print(""
          "_" * 50)
    menu1 = input("\n*TYPE THE NUMBER OF YOUR DESIRED CHOICE*"
                  f"\n1. {boldening('CREATE')} text file"
                  f"\n2. {boldening('ACCESS')} existing text file"
                  f"\n3. {boldening('EXIT')} THIS PROGRAM"
                  "\n>>>")
    while menu1 != int:
        try:
            menu1 = int(menu1)
            if 0 < menu1 < 4:
                break
            else:
                int("#Force Fail")
        except ValueError:
            menu1 = input(f"\nEnter 1 to {boldening('CREATE')}"
                          f"\nEnter 2 to {boldening('ACCESS')}"
                          f"\nENTER 3 to {boldening('EXIT')}"
                          "\n>>>")

    if menu1 == 3:
        print("\nI hope you enjoyed your time in this program")
        quit()

    while menu1 != "ENDING":

        first_line = True
        holder = open("File_Holder.txt", "r")
        print("\n" + boldening(holder.read()[63:]))
        holder.close()

        input(boldening("PRESS ENTER"))

        print(f"\n{Useful_Tools.Color.bold}{Useful_Tools.Color.red}DO NOT include PERIODS in name of this file."
              f"\nAny PERIODS will be removed, meaning you do not have to worry about adding the extension."
              f"\nThe '.txt will be added automatically{Useful_Tools.Color.end}"
              "\nAny SPACES you add will be replaced with '_'")
        sleep(1)

        if menu1 == 1:
            reads = input("\n\nWhat would you like to name this file?"
                          "\n>>>").replace(".", "").replace(" ", "_")
            read = reads + ".txt"
            holder = open("File_Holder.txt")
            if re.search(fr'{read}', holder.read()):
                print("\nIt looks like there is a file with this name already."
                      "\nI will now take you back to the main menu"
                      "\nCheck your " + boldening("Spelling"))
                break

            else:
                reading = open(f"{read}", 'w')
                print(f"\nAlright, the file with the name '{read}' has been created.")

        elif menu1 == 2:
            while menu1 != "END":
                reads = input(f"\n\nWhat is the name of the file you wish to {boldening('ACCESS?')}"
                              "\n>>>").replace(".", "").replace(" ", "_")
                read = reads + ".txt"
                try:
                    reading = open(f"{read}", "r")
                    menu1 = "ENDING"
                    break
                except FileNotFoundError:
                    do = input("\nThis file name seems to be non existent."
                               "\nWould you like to:"
                               f"\n1. Try {boldening('AGAIN')}"
                               f"\n2. {boldening('CREATE')} this file"
                               "\n>>>")
                    while menu1 != "END":
                        try:
                            menu1 = int(menu1)
                            if 0 < menu1 < 3:
                                break
                            else:
                                int("#Force Fail")
                        except ValueError:
                            menu1 = input(f"\nEnter 1 to try {boldening('AGAIN')}"
                                          f"\nEnter 2 to {boldening('CREATE')} this file"
                                          "\n>>>")

                    if menu1 == 1:
                        print("Okay.")

                    elif menu1 == 2:
                        reading = open(f"{read}", 'w')
                        print(f"Alright, the file '{read}' has been created")
                        break

        holder = open("File_Holder.txt", "a")
        holder.write(read + '\n')
        holder.close()

        while menu1 != "END":
            reading.close()
            menu2 = input("\n*TYPE THE NUMBER OF YOUR DESIRED CHOICE*"
                          f"\n1. {boldening('READ')} File"
                          f"\n2. {boldening('APPEND')} File"
                          f"\n3. {boldening('OVERWRITE')} File"
                          f"\n4. {boldening('EXIT')} Menu"
                          "\n>>>")
            while menu2 != int:
                try:
                    menu2 = int(menu2)
                    if 0 < menu2 < 5:
                        break
                    else:
                        int("#Force Fail")
                except ValueError:
                    menu2 = input(f"\nEnter 1 to {boldening('READ')}"
                                  f"\nEnter 2 to {boldening('APPEND')}"
                                  f"\nENTER 3 to {boldening('OVERWRITE')}"
                                  f"\nENTER 4 to {boldening('EXIT')}"
                                  "\n>>>")

            if menu2 == 4:
                menu1 = "ENDING"
                break

            if menu2 == 1:
                reading = open(read, "r")
                print(f"\nHere are the contents of the {read} file:\n"
                      f"\n{reading.read()}")

            if menu2 == 2:
                append = input(f"\nWhat would you like to add to the file? {boldening('(ONE LINE AT A TIME UNFORTUNATELY)')}"
                               "\n>>>")
                reading = open(f"{read}", "a")
                reading.write(append + "\n")

            if menu2 == 3:
                sure = input(f"\n{Useful_Tools.Color.red}{boldening('Are you sure you want to OVERWRITE the text in this file? (Y or N)')}"
                             "\n>>>").title()

                if sure == "Y":
                    write = input(f"\nNow, what would you like to add to this file? {boldening('(ONE LINE AT A TIME UNFORTUNATELY)')}"
                                  "\n>>>")
                    reading = open(f"{read}", "w")
                    reading.write(write + "\n")

                else:
                    print("\nGood thing I asked.")
