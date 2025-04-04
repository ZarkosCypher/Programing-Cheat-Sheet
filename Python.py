
print("Hello, World!")

print("-" * 50)
#Will print - 50 times one after the other exactly as within the "quotes"

#This program will print out "this will print Hello, World!" without the quotes. 
h = "Hello"
w = "World"
print(f"this will print {h}, {w}!")
#The f-string eg f"..." tells Python to interpret {} placeholders as expressions to be evaluated.
a = 2.01
b = 5
print(f"this will print a float 2.0 {a:.1f} and this can also print regular integers {b}.")
#The colon -> : is a format specifier for how a value should be displayed 
#The .1f specifies how to format the code 
#.1 means show 1 digit after the decimal point 
# The f at the end of .1f means format as a floating point number 

# This list is going to hold 2 values per slot so leg[1] is going to equal miles[1] and gas[1]  
leg = []
miles = 12
gas = 4
for i in range(2):
  miles += i
  #You can also do something like miles = miles + i
  gas += i
  leg.append((miles, gas))
for i, (miles, gas) in enumerate(leg, 1):
#Pyhton has a enumerate() function with tuple unpacking 
#1 The leg list is a list of tuples, where each tuple contains 2 values (miles, gas)
#Example: leg = [(2.1, 3.2), (4.5, 6.5)]
#2 The enumerate() function goes by enumerate(iterable value, start index) generates pairs of (index value) for each item in the iterable 
#The start parameter "1" sets the starting index because, without it, the starting index would be 0
#Example: (1, (200, 10)) is the first item
        #(2, (300, 12)) is the second item
#3 The for loop unpacks each pair from enumerate() in to two variables, i gets the index 1, 2 ...

  
#This is a simplified version of 
for i in range(len(leg)):
  miles = leg[i][0]
  gas = legs[i][1]
