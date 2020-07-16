#!/usr/bin/env/python3

userinput = float(input("Please enter your score to know the grade: "))

if userinput > 100:
    print("Come on, you can't have a score greater than 100 :)")
    userinput = float(input("Please enter your score to know the grade: "))
if userinput >=90:
    print("Congrats, its Grade A")
elif userinput >=80:
    print("Congrats, its Grade B")
elif userinput >=70:
    print("You got  Grade C")
elif userinput >=60:
    print("Its Grade D")
elif userinput <=59:
    print("Better luck next time, you got Grade E")
