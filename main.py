# variable = a container for a value. Behaves as the value that it

#first_name = "jacob"
#last_name = "charbonneau"
#full_name = first_name +" "+ last_name
#print(type(name))
#print("Hello "+full_name)

#age = 13
#age += 1
#print("Your age is: "+str(age))
#print(type(age))

#height = 250.5
#print("your height is: "+str(height)+"cm")
#print(type(height))

#human = True
#print("Are you a human: "+str(human))
#print(type(human))

#name = "Jacob"

#print(len(name))
#print(name.find("j"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count('o'))
#print(name.replace("J","C"))
#print(name*3)

#type casting = convert the data type of a value to another data type

#x = 1
#y = 2.0
#z = "3"

#x = float(x)
#y = float(y)
#z = float(z)

#print("X is "+str(x))
#print("Y is "+str(y))
#print(z)


#name = input("what is your name?: ")
#age = int(input("how old are you?:"))
#height = float(input("how tall are you?:"))

#print("Hello"+" "+ name)
#print("You are "+str(age)+" year old")
#print("You are "+str(height)+"cm tall")


#import math

#x = 1
#y = 2
#z = 3


#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(420))
#print(max(x,y,z))
#print(min(x,y,z))

#slicing = create a substring by extracting elements from another string
#          indexing[] or slice()
#          [start:stop:step]

#name = "Jacob Charbonneau"

#first_name = name[:5]
#last_name = name[5:17]
#funky_name = name[::3]
#reversed_name = name[::-1]

#print(reversed_name)

#website1 = "http://google.com"
#website2 = "httpe://wikipedia.com"


#slice = slice(7,-4)

#print(website[slice])

#age = int(input("how old are you?: "))

#if age == 100:
    #print("You are old!")
#elif age >= 18:
    #print("you are an adult!")
#elif age < 0:
    #print("you haven't been born yet!")
#else:
    #print("You are a child!")


#logical operators (and,or,not) = used to check if two or more conditional statement is true

#temp = int(input(' What day is it today?: '))

#if not(temp >= 0 and temp <= 30):
    #print(' Today is not your birthday ')


# while loop = a statement that will execute its block of code,
#              as long as its condition remains true


#name = ""

#while len(name) ==0:
    #name = input("Enter you name:")

#print("Welcome back "+name)


#for loop=   a statement that will execute its block of code
#            a limited amount of times
#
#            while loop = unlimited
#            for loop = limited


#for i  in range(10):
    #print(i+1)

#for i in range (50,100+1,5):
    #print(i)

#for i in "jacob":
    #print(i)

#import time

#def countdown(t):
    
    #for seconds in range(t,0,-1):
        #print(seconds)
        #time.sleep(1)
        
    #print('happy new year!') 

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print('happy new year!')


    
import turtle
  
t = turtle.Turtle()
 
s = int(input("Enter the length of the side of the Square: "))
 
# drawing first side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
 
# drawing second side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
 
# drawing third side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
 
# drawing fourth side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree







import time

for seconds in range (10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")