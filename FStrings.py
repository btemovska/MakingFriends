age_in_words = "2 years"
age = 24
name = "Biljana"
# print(name + " is " + age + " years old") #TypeError: can only concatenate str (not "int") to str

print(name + f" is {age} years old") #Biljana is 24 years old

print(f"Pi is approx {22 / 7:12.50f}")
#Pi is approx 3.14285714285714279370154144999105483293533325195312

pi = 22/7
print(f"Pi is approx {pi:12.50f}")
#Pi is approx 3.14285714285714279370154144999105483293533325195312
