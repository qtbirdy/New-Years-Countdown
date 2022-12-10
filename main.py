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

#first_name = name[:4] #pc thinks theres already a zero
#last_name = name[5:17] 
#funky_name = name[::3] #step
#reversed_name = name[::-1] #backwards

#print(reversed_name)

#website1 = "http://google.com"
#website2 = "httpe://wikipedia.com"


#slice = slice(7,-4) #same thing just with a coma

#print(website[slice])

#age = int(input("how old are you?: "))

#if age == 100:
    #print("You are old!") #only executes if its true if not it skips to the next one
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
    #print('be sad')
#elif temp < 0 or temp > 30:
    #print('the temperature is bad today!')
    #print('stay inside!')

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


#for i  in range(10):       #i fro index
    #print(i+1)

#for i in range (50,100+1,5):    #(using slicing)
    #print(i)

#for i in "jacob":
    #print(i)

#import time
    
#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print('happy new year!') 

# nested loops =  the "inner loop" will finish all of its iterations before 
#                 finishing one interation of the "outer loop"

#rows = int(input("How many rows?: "))
#columns = int(input("how many columns?: "))
#symbol = input("enter a symbol to use: ")

#for i in range(rows):
  #  for j in range(columns):
   #     print(symbol, end="")
  #  print()

# ============== Improvements ==============
# Replace "i" and "j" with underscores when a variable isn't used. e.g. for _ in range(): ...
#for _ in range(rows):
    #for _ in range(columns):
        #print(symbol, end="")
   # print()

# Instead of adding end="", build a list first that contains the content of the row you want to print
# then convert the list into a string, by combining (joining elements) of that list with an empty string
#for _ in range(rows):
    #my_row_items = []
    #for _ in range(columns):
  #      my_row_items.append(symbol)
   # my_row_items_as_a_string = "".join(my_row_items)
   # print(my_row_items_as_a_string)
    
# (more advanced) Do all of the above + use a list comprehension when you can for speedups in computation
#for _ in range(rows):
    #print("".join([symbol for _ in range(columns)]))




# Loop Control Statement = change a loops execution from its normal sequence

# break =         used to termiante the loop entirely
# continue =      skips to the next iteration of the loop.
# pass =          does nothing, acts as a placeholder

#while True:            #<break> exemple
   #name = input("enter your name: ")
   # if name != "":
  #      break

#phone_number = "123-613-7890"   #exemple of <continue>

#for i in phone_number:
    #if i == "-":
  #      continue
 #   print(i, end="")


#for i in range(1,21):        #exemple of <pass>
    
   # if i == 13:
  #      pass
  #  else:
   #     print()



#list = used to store multiple items in a single variable 

#food = ["pizza","pasta","fries","ice cream"]

#food[0] = "sushi"

#food.append("carrots")   #ect of fonctions
#food.remove("pasta")

#print(food[0])

#for x in food:
#    print(x)


#food = ["pizza","pasta","fries","ice cream"]

#for x in food:
 #   print(x)

# menu = int(input("What would u like 0,1,2,3?: "))

#if menu == 0:
#    print("voila: 🍕")         # Program i did for fun XD
#elif menu == 1:
 #   print("voila: 🍝")
#elif menu == 2:
#    print("volia: 🍟")
#elif menu == 3:
 #   print("volia: 🍦")
#else:
#    print("Not in the menu yet sorry:(")



# 2D lists = a list of lists

#drinks = ["coffee","soda","tea"]
#dinner = ["pizza","hamburger","hotdog"]
#dessert = ["cake","ice cream"]

#food = [drinks,dinner,dessert]

#print (food[1][2])


#tuple = colletion wish is ordered and unchangeable
#        used to group together realted data

#student = ("jacob",15,"male")

#print(student.count("jacob"))
#print(student.index('male'))

#for x in student:      #using for loops
 #   print(x)

#if "jacob" in student:       #using if statements
 #   print("jacob is here!")   


#set = colletion wich is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}

utensils.add("napkin")
utensils.rewmove("fork")
#utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)

for x in utensils:
    print(x)

# dictionary is NEXTTT

