meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""

print(meal1) #spameggsbeans
print()
print(meal2) #spam eggs beans
print()
print(meal3) #spam, eggs, beans
print()
print(meal4) #spam eggs beans

print("Terry\tJohn\tGraham\tMichael\tEric\tTerry")
first_name = "John"
last_name = "Cleese"
age = 78

# print(first_name + last_name + age) #error numerical values can't be added to strings.

a = 45
b = 15
c = 3
print(a - b / c)

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5
Total = total + tax
print(total)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5]) #MTWTFSS The slice starts at the first character, and includes every 5th character.


data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5]) #12345678

flower = "blue violet"
print('blue' in flower) #True

flower = "rose"
colour = "red"
print("The {0} is {0}".format(flower,colour)) #The rose is rose
print("The {1} is {0}".format(flower,colour)) #The red is rose
print("The {0} is {1}".format(colour, flower)) #The red is rose
print("The {0} is {1}".format(flower, colour)) #The rose is red