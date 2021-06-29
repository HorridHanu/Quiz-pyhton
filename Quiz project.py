#CODE LANGUAGE IS PYTHON
#CODE BY HANU
#EDUCATIONAL PURPOSE ONLY!
#PROGRAME DATE : 29/JUNE/2021
#CODE FOR QUIZ.

print("\n\t\t\t!<QUIZ>!")
print("\n\t!!!Welcome Answer These Questions!!!")
total = 0
print("~Each question have 5 marks.")


print("A.Python is ____ language?")
print("1.compiler ")
print("2.interpreted ")
print("3.both ")
print("4.none")
ans= int(input("Enter the ans 1: "))
if ans==2:
    total=total+5


print("A.Tuple is ____?")
print("1.immutable ")
print("2.mutable")
print("3.both ")
print("4.none")
ans= int(input("Enter the ans 2: "))
if ans==1:
    total=total+5


print("A.Java is used for____?")
print("1.website making")
print("2.andorid development")
print("3.both ")
print("4.none")
ans= int(input("Enter the ans 3: "))
if ans==2:
    total=total+5


print("A.This sysmol % is used for")
print("2.multiply ")
print("2.divide")
print("3.modulous")
print("4.none")
ans= int(input("Enter the ans 4: "))
if ans==3:
    total=total+5

print("Your score is : ",total)
if total<=20:
    print("Hurre! your 4 ANSWER is right.")
if total<=15:
    print("Yeah! your 3 ANSWER is right.")
if total<=10:
    print("Not bad! your 2 ANSWER is right.\nDo better next time!")
 if total<=5:
    print("Oh no! your only 1 ANSWER is right.\nTry again!")