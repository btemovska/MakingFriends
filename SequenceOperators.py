string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords") # don't need the + sign to concatenate
print("Hello " * 5)  # Hello Hello Hello Hello Hello
# print("Hello " * 5 + 4) #operaror precedence error
print("Hello " * (5+4)) #Hello Hello Hello Hello Hello Hello Hello Hello Hello
print("Hello " * 5 + "4") #Hello Hello Hello Hello Hello 4

today = "friday"
print("day" in today) #True
print("fri" in today) #True
print("thur" in today) #False
print("parrot" in "fjord") #False
