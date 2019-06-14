'''a=eval(input("Enter marks:"))
if a>89:
    print("Grade: O")
elif a>79 and a<90:
    print("Grade: A")
elif a>69 and a<80:
    print("Grade: B")
elif a>59 and a<70:
    print("Grade: C")
elif a>49 and a<60:
    print("Grade: D")
elif a>39:
    print("Grade: E")
else:
    print("Grade: F")'''



'''filepath="C:\\filename.txt"
file=open(filepath,"r")
#lines=file.read()
lines=file.readlines()
print(lines)
print(type(lines))
file.close()
file=open(filepath,"a")
file.write("\nPython is amazing")
file.close()
file=open(filepath,"r")
lines=file.read()
#print(lines)
print(lines.splitlines())
file.close()'''


'''def printmyname():
    print("My name is Shatrunjay")
printmyname()'''


'''def compare(a,b):
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")
a,b=eval(input("Enter two numbers:"))
compare(a,b)'''



'''def printmyname(count=5):
    for i in range(5):
        print("Shatrunjay")
printmyname(20)'''


'''def increment(x):
    print("Beginning execution of increment, x=",x)
    x+=1
    print("Ending execution of increment, x=",x)
    return x
def main():
    x=5
    print("Before increment, x=",x)
    x=increment(x)
    print("After increment, x=",x)
main()'''


'''fruits={}
fruits={"A":"Apple","B":"Banana","C":"Chikoo"}
print(fruits)
fruits["M"]="Mango"
print(fruits)
print(fruits["B"])
fruits_new={"G":"Grapes","P":"Papaya"}
fruits.update(fruits_new)
print(fruits)
berry={"S":"Strawberry","B":"Blueberry","M":"Mulberry","G":"Gooseberry"}
fruits["Berries"]=berry
print(fruits)'''









