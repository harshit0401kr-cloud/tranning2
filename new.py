##python was created by guedo ban rossum


# print("i am learning python")

# print(18)

# a="harshit"
# print(a)
# print(type(a))


#special characters are not allowed in variable name
# ---->(# @ %) 
#exception (------>  _ ) are allowed 
# (0 - 9)----->are not allowed  

#(A to Z)-----> are allowed 

#camel case = myName

#snake case = _my_name

#MyNameIs = pascal case

# myname= "harshit"
# print(myname)

# MyRoll= 62
# print(MyRoll)


# x=8
# y="harshit"
# print(type(x))
# print(type(y))


#arthemetic operators
# a = 26
# b=10
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a**b)
# print(a//b)


# assignment operators
# a =85
# b=144
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

#Logical operators

# x=5
# y=10
# print(x and y)
# print(x or y)
# print(not x)
# print(not y)
# print()



#bitwise operators
# a = 6 #110 in binary
# b = 3 #011 in binary
# print(a & b)  # Bitwise AND
# print(a | b)  # Bitwise OR
# print(a ^ b)  # Bitwise XOR
# print(~a)     # Bitwise NOT
# print(a << 1) # Left Shift
# print(a >> 1) # Right Shift



#assignment operators
#x=10
# x+=3
# print(x)
# x-=2
# print(x)
# x*=2
# print(x)
# x/=2
# print(x)
# x%=3
# print(x)


#membership operators
# nums = [1, 2, 3, 4, 5]
# print(3 in nums)  # True
# print(10 in nums)  # False
# print(10 not in nums)  # True


#identity operators
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# print(a is b)  # True
# print(a is c)  # False
# print(a is not c)  # True

# a = 10
# b=4
# print(a & b)  # Bitwise AND
# print(a | b)  # Bitwise OR
# print(a ^ b)  # Bitwise XOR
# print(~a)     # Bitwise NOT
# print(a << 1) # Left Shift
# print(a >> 1) # Right Shift

 
###################################   DAY2     ################################


#data type in python
# (1)-----Numeric: Intiger ,Float,complex
# (2)-----sequence : string , list , tuple
# (3)-----dictionary 
# (4)-----set
# (5)-----boolean
# (6)-----binary: bytes,bytearray,memoryview


# a =54
# b=56
# print(a+b)

# my_class = complex(2,3)
# print(type(my_class))


#sequence data type
#B1 = string ()
#B2 = List[]
#B3 = tuple()
# b1= "harshit"
# print(type(b1))
# a3 = complex(2,3)
# print(type(a3))
# a = [2,3,4,5,6,xyz]
# print(type(a))
# l = (1,2,3,4)
# print(type(l))
#my_dictionary = {"name":"harshit","age":22}
#print(type(my_dictionary))

##variable name rules
# _myname= "harshit"
# print(_myname)
# myname="harshit"
# print(myname)
# myName= "harshit"
# print(myName)
# _my_name="harshit"
# print(_my_name)

# MyNameIs="harshit"
# print(MyNameIs)

# a = [2,3,4,5,6,"xyz"]
# print(a)

# a.append("harshit")
# print(a)

# a.insert(2,"harshit")
# print(a)

# a.remove("xyz")
# print(a)

# a.pop()
# print(a)

# del a[2]
# print(a)

# print(len(a))
# print(min(a))
# print(max(a))



# a[2]
# print(a[2])

# b3=(1,2,3,44,"harshit")
# print(type(b3))
# print(b3)

# my_dictionary = {"name":"harshit","age":18,'city':"siwan",'college':"saitm",'branch':"computer science"}
# print(type(my_dictionary))
# print(my_dictionary)

# my_set = {1,2,3,4,5,"harshit"}
# print(type(my_set))
# print(my_set)


#######IF ELSE STATEMENTS################

# age = int(input("enter your age: "))
# if age <13:
#     print("you are a child")
# elif age < 18:
#     print("you are a teen ager")
# elif age < 60:
#     print("you are an adult")
# else:
#     print("you are a senior citizen")


# age = 16
# if age >= 18:
#     print("you can vote")
# else:
#     print("you cannot vote")

# marks = 85
# if marks >=90:
#     print("Grade: A+")
# elif marks >=80:
#     print("Grade: A")
# elif marks >=70:
#     print("Grade: B")
# else:
#     print("Grade: C")


##nested if
# num = 12
# if num > 0:
#     if  num %2 == 0:
#         print("Positive Even Number")
#     else:
#         print("Positive odd number")
# else:
#     print("Number is Negative")


#     ##short hand if
# x = 20
# if x > 10: print("x is greater than 10")

####short hand if else
# a , b  = 10,20
# print("a is greater") if a > b else print("b is greater")






# def star_pyramid(n):
#     for i in range(1, n +1):
#         print(" "*(n-i)+"*"*i)

# star_pyramid(5)


# import turtle 
# screen = turtle.Screen()
# screen.bgcolor("black")

# pen = turtle.Turtle()
# pen.color("white")
# pen.speed(8)
# pen.width(5)

# pen.begin_fill()
# pen.fillcolor("red")

# for _ in range(100):
#     pen.forward(200)
#     pen.right(170)

# pen.end_fill()
# turtle.done()

# pen.hideturtle()

# turtle.done()

##creating a cycle

# import turtle
# screen = turtle.Screen()
# screen.bgcolor("white")

# pen = turtle.Turtle()
# pen.speed(8)
# pen.width(5)
# pen.color("red")

# def draw_wheel(x,y):
#     pen.penup()
#     pen.goto(x,y)
#     pen.pendown()
#     pen.circle(50)

# draw_wheel(-100,-100)
# draw_wheel(100,-100)


# pen.penup()
# pen.goto(-100, -100)
# pen.pendown()
# pen.goto(0, 0)
# pen.goto(100, -100)
# pen.goto(-50, -100)
# pen.goto(0,0)


# pen.penup()
# pen.goto(100, -100)
# pen.pendown()
# pen.goto(130, -50)
# pen.goto(110, -50)

# pen.penup()
# pen.goto(0,0)
# pen.pendown()
# pen.goto(-20, 20)
# pen.goto(-40, 20)

# pen.hideturtle()
# turtle.done()

##tuples are not changable
#tuples  are always start from ().

# my_tuple = (1,2,3) ##simple tuple
# my_tuple = (2,"hello",3) ##mixed tuple
# my_tuple = (5,) ##single element tuple
# t = (10,20,30)
# print(t[0])
# print(t[-1])

# my_tuple = (1,2,3,4,5)
# print(my_tuple)

# my_tuple = (2,"hello",3)
# print(my_tuple)

# my_tuple = (5,)
# print(my_tuple)

# a=(1,2)
# b= (10,30)
# print(a+b)
# print(a*5)

# a = ("it's rainy day \nyou are a bad man")#\n is used for new line
# print(a)

# a = ("it's a rainy day \t your are a bad man")#\t is used for tab space
# print(a)

# a = ("it's a rainy day      you are a bad man")#multiple space
# print(a)

# a = ("it's a rainy day      you are a bad man")#multiple space
# print(len(a))
# print(a.find("rainy"))

# a ="1"
# b="3"
# print(a+b)

# x="harshit singh\t"
# print(x*5)

# a = ("it's a rainy day      you are a bad man")#indexing string
# print(a[-11])

# a = ("it's a rainy day      you are a bad man")#slicing string
# print(a[6:-11])

# a = ("it's a rainy day      you are a bad man")#membership operator
# print("rainy" in a)

# a = ("it's a rainy day      you are a bad man")#lower case string
# print(a.lower())

# a = ("it's a rainy day      you are a bad man")#upper case string
# print(a.upper())

# a = ("it's a rainy day      you are a bad man")#capitalize string
# print(a.capitalize())

# a = ("it's a rainy day      you are a bad man")#title case string
# print(a.title())

# a = ("it's a rainy day      you are a bad man")#strip string
# print(a.strip())

# a = (" 'Hello World' ")#strip string
# print(a.strip())

# a = ("hello") #string concatenation
# print(a)

# a = ("it's a rainy day you are a bad man")#replace string
# print(a.replace("bad","good"))

# a = ("it's a rainy day you are a bad man")#find string
# print(a.find("r"))

# a = ("it's a rainy day you are a bad man")
# print(a.find('h'))

# a = ("it's a rainy day you are a bad man")#count string
# print(a.count('a'))

# a = ("it's a rainy day you are a bad man")
# print(a.startswith("a"))

# a = ("it's a rainy day you are a bad man")
# print(a.lstrip("a").startswith("a"))

# a = ("it's a rainy day you are a bad man")
# print(a.lstrip("a").startswith("i"))

# a = ("it's a rainy day you are a bad man")
# print(a.rstrip("a").startswith(" "))

# you = "you are a person of aura" #split(sepptate words from a sentence)
# me = you.split()
# print(me)

# import sys 
# a = []
# for i in range(10):
#     a.append(i)
#     print(sys.getsizeof(a))
# myName = "harshit"#camel case

# _my_name= "harshit singh"#snake case 

# MyNameIs = "harshit singh"#pascal case
# myname = "harshit singh"#lower case


##################################### DAY3 #############################################################################


# import time

# timestamp=time.strftime('%H:%M:%S')
# print(timestamp)

# timestamp = int(time.strftime('%H'))
# print(timestamp)

# timestamp = int(time.strftime('%M'))
# print(timestamp)

# timestamp= int(time.strftime('%S'))
# print(timestamp)


#####basic calculator using function

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")
# if operation == "+":
#     print("Result:" +(num1 + num2))
# elif operation == "-":
#     result = num1 - num2
#     print(f"Result: (num1 - num2)")
# elif operation == "*":
#     result = num1 * num2
#     print(f"Result: {result}")
# elif operation == "/":
#     result = num1 / num2
#     print(f"Result: {result}")
# else:
#     print("Invalid operation")




#####weather suggestion##

# weather = input("Enter the weather (sunny, rainy, snowy): ").lower()
# if weather == "sunny":
#     print("wear sunglass")
# elif weather == "rainy":
#     print("carry an umbrella")
# elif weather == "cold":
#     print("wear a jacket")
# else:
#     print("i don't know that weather type.")
    

################################################ 


###traffic light
# light = input("Enter the traffic light color (red, yellow, green): ").lower()
# if light == "red":
#     print("stop")
# elif light == "yellow":
#     print("get ready")
# elif light == "green":
#     print("go")
# else:
#     print("invalid traffic light color")


###Loops in python
##### what is loop?
## A LOOOP ECCUTES A BLOCK OF CODE MULTIPLE TIMES TO RUN  (WORKS WITH LIST , TUPLESTRING , DICTIONARY , RANGE)


# for i in range(5):
#     print("hello", i)


##2.while loop
# used when we don't know exact repetitions: runs untill condition is false.
# count = 1
# while count <= 5:
#     print("hello", count)
#     count += 1


#### 3. loop control 
## break --> exit loop immediately
##continue -> skip current iteration

#pass -->> do nothing (placeholder)

# for i in range (1,6):
#   if i == 3:
#        continue
#   if i == 5:
#        break
#       print(i)


####4. nested loops
# loop inside another loop
# for i in range (2):
#     for j in range (3):
#         print("i = ", i,"j  = ",j)


###SUMARY
#for loop------------------> repeat over sequence 
#while  loop --------------> repeat while condition true
#break, continue,pass------> control flow
#nested loops -------------> loop inside Loop

####loop>>>
# A LOOP IS A PROGRAMMING CONSTRUCT THAT REPEATS  A BLOCK OF CODE MULTIPLE TIMES UNTIL A CONDITION IS MET
#(OR UNTIL THE ITEMS TO ITERATE ARE EXHAUSTED)
# LOOPS LET YOU AUTOMATE REPETITIVE TASKS: PROCESSING EVERY ITEM IN A LIST,SCANNING
# LINES IN A FILE, AGGREGATING NUMBERS,ETC.


#PYTHON HAS TWO MAIN LOOP TYPES:

# FOR - ITERATE OVER AN ITERATE (LIST,TUPLE,STRING,DICT,GENERATOR,FILE,--).

# WHILE -- REPEAT WHILE A CONDITION REMAINS TRUE.
##  FOR LOOP - CONCEPT & USAGE


# A FOR LOOP PULLS ITEMS FROM AN KTERABLE ONE BY ONE.
# fruits = ["aple", "banana", "cherry"]
# for f in fruits:
#     print(f)        ## print each fruits

#ITERABLE VS INTERATORS(BRIEF)

# ITERABLE : AN OBJECT YOU CAN LOOP OVER (IM[PPLEMENTS__ ITER__ OR SEQUENCE PROTOCOL])-- E.G,LIST,STR,DICT

# INTERATOR : AN OBJECT WITH__NEXT__()AND __ITER__();CALLING NEXT() ADVANCES IT UNTI STOPITERATION.

# you can manually use interator protocal:
# it = iter([1,2,3])
# print(next(it)) #1
# print(next(it)) #2
# print(next(it))


#q.2
# for i in range(1,10):
#     print(i)

##q.2
#i= 10
# while i >=1:
#     print(i)
#     i -= 1

#q.3
# for i in range(1,11):
#     print(5*i)

##q.4
# num = 1
# while num <= 20:
#     if num % 2 == 0:
#         print(num)
#     num +=1


#q.5
# rows = 50
# for i in range(1,rows+1):
#     for j in range(i):
#         print("<>",end=" ")
#     print()



########################  >>>>> PANDAS <<<<< ################

# data frame in pandas
#create  data frame 
# import pandas as pd
# df = pd.DataFrame(["harshit","kumar","singh"],columns= ['harshit details'])
# print(df)
# print(type(df))


# import pandas as pd
# details = {
#     'name': ["Harshit",'Arti','Anushka','kushagra','naveen','mahima','rishabh'],
#     'age': [18,17,20,26,30,44,52],
#     'salary': [100000,12000,23000,20000,28000,27600,30000]
# }
# df = pd.DataFrame(details)
# print(df)

#basic DataFrame understanding
#df.head()#top rows by default 5 top rows
#df.head()

#df.tail()# by default last 5 low rows

#df.shape # to know columns and rows in a data

#df.columns

#df.rename(columns=('salary':'payment')),implace = true

#df.info()# for information
#df.describe()# for stastical summary

# import pandas as pd
# details = {
#     'name' : ['Harshit','Arti','Anushka','kushagra','naveen','mahima','rishabh','sonnu','monu','rakesh','raju','bihari','nigam','singh','rahul'],
#     'age': [18,17,20,26,30,44,52,24,25,26,28,29,23,30,27],
#     'salary': [100000,12000,23000,20000,28000,27600,30000,26000,26666,40000,30000,35000,33000,24000,50000]
# }
# df = pd.DataFrame(details)
# print(df)

# df.head


### save and load data frame from csv

# df.to_csv('new_data.csv')
# pd.read_csv(r"c:\Users\harsh\Desktop\newpython\new_data.csv")  ###for file location

#df.to_csv('new_data.csv' , index = False) ## to remove index number

# df.read.csv(r"C:\users\kdev2\new_data.csv)


###################################################  >>>>> DAY 4 <<<<< #######################################################
 

#pd.read_csv(r"c:\Users\harsh\Desktop\newpython\new_data.csv")  ###for file location

# df.loc[df.name=='harshit']

# df.iloc[0] ##index value based

# df.iloc[0:5] ## lost vallue never be include in iloc

# df.iloc[3]

# df['age']>=20  ## value always  find in boolean

# df(df('age') >= 20) & (df('payment')>=10000)

# df.where(df('age')>= 24)

# df.where(df('age') >= 24,other = 'not eligible')

# df['team']=["ceo",'hr','clo','accountant','developer','marketing','boss']

# df.loc(6,'salary')=50000 ## update value using index name

# df.loc(df.name == 'Harshit','payment')= 1000000000000000

# df.drop(df[df.name == 'xyz'].index) #drop  row axis = 0

# df.drop(1, axis = 0) ## by index number

# df.drop('Bonus',axis=1)

#df.drop('Bonus'axis=1,inplace=True)

#df=df.drop(df(df.name == 'xyz')) #drop row axis =0

#df = df.drop(df(df.name == 'xyz').index) # drop row axis == 0


#####################################################>>>>>>>>>>> DAY 5 <<<<<<<<<########################################################

