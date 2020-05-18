# Jared Jackson
# 5.17.2020
# In this program I will play around with the reading, writing, and appending of files
from time import sleep
import Useful_Tools

input("PRESS ENTER")

name = input("\nWhy hello there user, what is your name?"
             "\n>>>").title()
sleep(.5)

print(f"\nWelcome {name}."
      f"\nToday we are going to be checking out a new program."
      f"\nYou will be able to..."
      f"\nWait.")

#sleep(2)
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
    #sleep(.5)
    print(dots[0:num])
    num += 1
num = 2
while num > 0:
    #sleep(.5)
    print(dots[0:num])
    num -= 1
#sleep(.5)

print("\nYou know what?"
      "\nI'll just make a new program!"
      "\nIt'll be about.."
      "\nUhh, Reading and Writing.."
      "\nYeah, Reading and Writing to a file")
# sleep(5)

print("\nThere won't be much to variation in this program, "
      "but you'll have freedom to do whatever"
      "\nI will have a menu that will allow any user to:"
      "\nCREATE a text file"
      "\nACCESS an existing text file"
      "\nREAD the contents of that text file"
      "\nAPPEND (ADD) new context to the end of that text file"
      "\nOVERWRITE the contents of that text file")


input("\n\n*PRESS ENTER IF YOU UNDERSTAND*")

print("\nAlright! This should be fun."
      "\nOui, something fun you can do is make Journal Entries")

menu = 'START'
read = 0
reading = 0
# Text_Files_List = []  # I want to a list that will Keep track of the files created,
                        # but I will need to figure out how to access the contents of the list after the program has ended
while menu != "END":
    print(""
          "_" * 50)
    menu1 = input("\n*TYPE THE NUMBER OF YOUR DESIRED CHOICE*"
                  "\n1. CREATE text file"
                  "\n2. ACCESS existing text file"
                  "\n3. EXIT THIS PROGRAM"
                  "\n>>>")
    while menu1 != int:
        try:
            menu1 = int(menu1)
            if 0 < menu1 < 4:
                break
            else:
                int("#Force Fail")
        except ValueError:
            menu1 = input("\nEnter 1 to CREATE"
                          "\nEnter 2 to ACCESS"
                          "\nENTER 3 to EXIT"
                          "\n>>>")

    if menu1 == 3:
        print("\nI hope you enjoyed your time in this program")
        quit()

    while menu1 != "ENDING":
        print(f"\n{Useful_Tools.Color.bold}{Useful_Tools.Color.red}DO NOT include PERIODS in name of this file."
              f"\nAny PERIODS will be removed, meaning you do not have to worry about adding the extension."
              f"The '.txt will be added automatically{Useful_Tools.Color.end}"
              "\nAny SPACES you add will be replaced with '_'")
        # sleep(4)

        if menu1 == 1:
            reads = input("\n\nWhat would you like to name this file?"
                          "\n>>>").replace(".", "").replace(" ", "_")
            read = reads + ".txt"
            reading = open(f"{read}", 'w')
            print(f"\nAlright, the file with the name '{read}' has been created.")

        elif menu1 == 2:
            while menu1 != "END":
                reads = input("\n\nWhat is the name of the file you wish to ACCESS?"
                              "\n>>>").replace(".", "").replace(" ", "_")
                read = reads + ".txt"
                try:
                    reading = open(f"{read}", "r")
                    menu1 = "ENDING"
                    break
                except FileNotFoundError:
                    do = input("\nThis file name seems to be non existent."
                               "\nWould you like to:"
                               "\n1. Try AGAIN"
                               "\n2. CREATE this file"
                               "\n>>>")
                    while menu1 != "END":
                        try:
                            menu1 = int(menu1)
                            if 0 < menu1 < 3:
                                break
                            else:
                                int("#Force Fail")
                        except ValueError:
                            menu1 = input("\nEnter 1 to try AGAIN"
                                          "\nEnter 2 to CREATE this file"
                                          "\n>>>")

                    if menu1 == 1:
                        print("Okay.")

                    elif menu1 == 2:
                        reading = open(f"{read}", 'w')
                        print(f"Alright, the file '{read}' has been created")
                        break

        while menu1 != "END":
            reading.close()
            menu2 = input("\n*TYPE THE NUMBER OF YOUR DESIRED CHOICE*"
                          "\n1. READ File"
                          "\n2. APPEND File"
                          "\n3. OVERWRITE File"
                          "\n4. EXIT Menu"
                          "\n>>>")
            while menu2 != int:
                try:
                    menu2 = int(menu2)
                    if 0 < menu2 < 5:
                        break
                    else:
                        int("#Force Fail")
                except ValueError:
                    menu2 = input("\nEnter 1 to READ"
                                  "\nEnter 2 to APPEND"
                                  "\nENTER 3 to OVERWRITE"
                                  "\nENTER 4 to EXIT"
                                  "\n>>>")

            if menu2 == 4:
                break

            if menu2 == 1:
                reading = open(read, "r")
                print(f"\nHere are the contents of the {read} file:\n"
                      f"\n{reading.read()}")

            if menu2 == 2:
                append = input("\nWhat would you like to add to the file? (ONE LINE AT A TIME UNFORTUNATELY)"
                               "\n>>>")
                reading = open(f"{read}", "a")
                reading.write(append + "\n")
                reading.close()

            if menu2 == 3:
                sure = input(f"{Useful_Tools.Color.bold}"
                             "\nAre you sure you want to OVERWRITE the text in this file? (Y or N)"
                             f"{Useful_Tools.Color.end}"
                             "\n>>>").title()

                if sure == "Y":
                    write = input("\nWhat would you like to add to this file? (ONE LINE AT A TIME UNFORTUNATELY)"
                                  "\n>>>")
                    reading = open(f"{read}", "w")
                    reading.write(write + "\n")

                else:
                    print("\nGood thing I asked.")
