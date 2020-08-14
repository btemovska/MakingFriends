age = 24
print("My age is " + str(age) + " years") #My age is 24 years
print("My age is {0} years".format(age)) #My age is 24 years

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
    #There are 31 days in Jan, Mar, May, Jul, Aug, Oct and Dec

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))
    #There are 31 days in Jan, Mar, May, Jul, Aug, Oct and Dec

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1},Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
#Jan: 31, Feb: 28, Mar: 31, Apr: 30, May: 31, Jun: 30,Jul: 31, Sep: 30, Oct: 31, Nov: 30, Dec: 31
