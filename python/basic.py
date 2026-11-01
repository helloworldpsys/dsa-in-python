print("hi i am learning now passionately everyything to be best coder")

x = 1
if x == 1:
   # indented four space
   print("x is 1")

   #variables and data type 
   #python is object oriented, no need to declare a var before using them, var are objects
   a = 7
   print(a)

   b = 8.7
   print(b)
   c = float(9)
   print(c)

   d = a+b
   print(int(d))


   #lists
   #same as array
   mylist = []
   mylist.append(1)
   mylist.append(2)
   mylist.append(3)
   print(mylist)
   print(mylist[1])

   for x in mylist:
      print(x)

   #operators
   p = 3+400/5-33*5
   print(p)  

   squared = 7 ** 2
   cubed = 2 ** 3
   print(squared)
   print(cubed)
 
   q = "hello "  *20
   print(q)

# %s - String (or any object with a string representation, like numbers)String manipulation tutorial
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
astring = "Hello world!"
print(astring.index("o")) 