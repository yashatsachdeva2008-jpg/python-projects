print("Welcome to grade calculator")
name=input("Enter your name:")
print("hello",name)
print()
print("please enter your marks-")
a=float(input("Enter makrs in 1st subject:"))
if a<0 or a>100:
    print("Marks u entered are invalid")
    quit()
b=float(input("Enter makrs in 2nd subject:"))
if b<0 or b>100:
    print("Marks u entered are invalid")
    quit()
c=float(input("Enter makrs in 3rd subject:"))
if c<0 or c>100:
    print("Marks u entered are invalid")
    quit()
d=float(input("Enter makrs in 4th subject:"))
if d<0 or d>100:
    print("Marks u entered are invalid")
    quit()
e=float(input("Enter makrs in 5th subject:"))
if e<0 or e>100:
    print("Marks u entered are invalid")
    quit()
total=a+b+c+d+e
percentage=(total/500)*100

if percentage>=90 :
    grade="A"
elif percentage<90 and percentage>=80:
    grade="B"
elif percentage<80 and percentage>=70:
    grade="C"
elif percentage<70 and percentage>=60:
    grade="D"
else:
    grade="Fail"

print("Students Name:",name)
print("Toatal marks:",total,"/500")
print("Percentage:",percentage,"%")
print("Grade:",grade)
