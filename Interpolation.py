#note this is old way of string formatting used in python 2, it will be stopped at some point
age = 24
print("My age is %d years" % age) #My age is 24 years

major = "years"
minor = "months"
print("My age is %d %s, %d, %s" % (age, major, 6, minor)) #My age is 24 years, 6, months
print("PI is approximately %f" % (22 / 7)) #PI is approximately 3.142857

print("PI is approximately %60.50f" % (22 / 7))
    #PI is approximately         3.14285714285714279370154144999105483293533325195312
