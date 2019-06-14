'''C=eval(input("Enter temperature:"))
F=C*9/5+32
print("Temperature in Farenheit is:",F)'''


'''name,sname,fname,mname=eval(input("Enter details:"))
print(sname,".",name,"&",fname,"@",mname)'''


'''a=eval(input("enter a number:"))
b=eval(input("Entes another number:"))
c=a>b
d=a==b
print("The expression is evaluated ",c, d," with type= ",type(c),type(d))'''


'''a=eval(input("Enter 1st number:"))
b=eval(input("Enter 2nd number:"))
c=eval(input("Enter 3rd number:"))
if(a>b) and (a>c):
    print("a is greater than b and c")
elif(b>a) and (b>c):
    print("b is greater than c and a")
else:
    print("c is greater than a and b")'''


'''a=eval(input("Enter 1st number:"))
b=eval(input("Enter 2nd number:"))
c=eval(input("Enter operator:"))
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)'''


'''count=eval(input("Enter number of repetitions:"))
while(count!=0):
    print("I will only code in python")
    count=count-1'''


'''count=eval(input("Enter the number of values:"))
a=0
b=0
while(a!=count):
    number=eval(input("Enter number:"))
    b=b+number
    a=a+1
print("Average is: ",b/a)'''


'''count=eval(input("Enter the number of repetitions:"))
for i in range(count):
    print(i)'''


'''for i in range(0,10,2):
    print(i)'''


'''s1="Orange"
s2="Banana"
for letter in s1:
    if letter in s2:
        print(s1,"and",s2,"share the letter",letter)'''


'''name="Shatrunjay"
print(len(name))
print(name[7])
print(name[-4])
print(name[3**2])
print(name[:])
print(name[1:])
print(name[:6])
print(name[:100])
print(name[1:-1])
print(name.upper())
print(name.find("jay"))
name.replace("jay","xyz")
print(name)'''


'''lst=[2,-3,0,4,-1]
print(lst)
lst[4]=12
lst[-2]=1
print
print(lst)
lst[1],lst[2]=eval(input("Enter values:"))
print(lst)'''


'''a=[1,2,3,4]
b=[5,6,7,8]
print(a+b)'''


'''a=list(range(0,100,4))
b=list(range(100,0,-5))
c=list(range(-20,10))
print(a)
print(b)
print(c)'''


'''a=[1,2,3,4,5]
b=a
c=[6,7,8,9,10]
print(b is a)
print(c is b)'''


'''a=list(range(0,20))
print(a[1:16])
a[2:5]=["x","y","z"]
print(a)'''


'''fruits=["Banana","Apple","Mango","Guava","Pineapple"]
fruits.append("Papaya")
fruits.extend(["Jackfruit","Grapes","Lichi"])
fruits.insert(2,"Orange")
fruits.remove("Apple")
print(fruits)
print(fruits.pop(2))
print(fruits.index("Guava"))'''


'''s1=[x*x for x in range(1,26)]
print(s1)
s1=[x*x for x in range(1,26) if x%10!=5]
print(s1)'''






