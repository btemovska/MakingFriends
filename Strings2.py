#         0123456789
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3]) #w (it is starting to count at 0)
print(parrot[4])
print(parrot[9]) #space
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-1]) #3 counting end of the string from -1 not -0
print(parrot[-14]) #N

print()
print()

print(parrot[-11])
print(parrot[-10])
print(parrot[-5]) #space
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# slicing without a step
print(parrot[0:6]) #start at 0 up to, but not include 6 #Norweg
print(parrot[3:5]) #we

print(parrot[0:9]) #Norwegian
print(parrot[:9]) #Norwegian
print(parrot[10:]) #Blue

print(parrot[:6] + parrot[6:]) #Norwegian Blue
print(parrot[:]) #Norwegian Blue

print(parrot[-4:2])  #can't go backwards
print(parrot[-4:-2]) #Bl
print(parrot[-4:12]) #Bl
print(parrot[-14:-8]) #Norweg

# slicing with skipping
print(parrot[0:6:2])  #Nre aka skip by 2
print(parrot[0:6:3])  #NW aka skip by 3

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators) #,;: ,;
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])  #[9, 223, 372, 36, 854, 775, 807]

#slicing backwards (bc the step/skip value is -1, the statt value has to be bigger then the stop value
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)  #zyxwvutsrqponmlkjihgfedcb
print(letters[::-1]) #zyxwvutsrqponmlkjihgfedcba this is true backwards

print()
print(letters[16:13:-1]) #qpo
print(letters[4::-1]) #edcba
print((letters[:17:-1])) #zyxwvuts

print(letters[-4:]) #last 4 letters
print(letters[-1:]) #last letter
print(letters[:1]) #first letter
print(letters[0]) #first letter
        #note though if the string is empty, no index can be accessed




