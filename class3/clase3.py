my_age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
complex_number = complex(input("Enter a complex number (e.g., 2+3j): "))

# Calculating the area of a triangle
base= float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

#Calculate perimeter of a triangle
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
side_c = float(input("Enter the length of side C: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)

# Get length and width of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

#get radius of a circle
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
# Calculate area and circumference
area = pi * radius ** 2
circumference = 2 * pi * radius
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)


# y = 2x-2 
#interception of the line with the y-axis is -2
#interception of the line with the x-axis is 1
p1 = 1 
p2 = 0 
p3 = 0 
p4 = -2

slope = (p2 - p4) / (p1 - p3)
print("The slope of the line is:", slope)
euclidean_distance = ((p1 - p3) ** 2 + (p2 - p4) ** 2) ** 0.5
print("The Euclidean distance between the points is:", euclidean_distance)

# between point (2, 2) and point (6,10)

x1 = 2 
x2 = 6
y1 = 2
y2 = 10
slope = (y2 - y1) / (x2 - x1)
print("The slope of the line is:", slope)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("The Euclidean distance between the points is:", euclidean_distance)

#compare the slopes of the two lines
slope1 = (p1 - p3) / (p2 - p4)
slope2 = (y2 - y1) / (x2 - x1)
if slope1 > slope2:
    print("The slope of the first line is greater than the slope of the second line.")  
elif slope1 < slope2:
    print("The slope of the first line is less than the slope of the second line.")
else:
    print("The slopes of the two lines are equal.")

# Bhaskara formula
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print("The roots are real and different:", root1, root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The root is real and repeated:", root)
else:
    print("The roots are complex.")

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = float(input("Enter the value of x: "))
y = x**2 + 6*x + 9
print("The value of y is:", y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
word1 = "python"
word2 = "dragon" 
if len(word1)<=len(word2):
    var = False 
else:
    var = True
print(var)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in word1 and 'on' in word2:
    print("The substring 'on' is found in both words.")

word3 = "I hope this course is not full of jargon"
if 'jargon' in word3:
    print("The word 'jargon' is found in the sentence.")

# There is no 'on' in both dragon and python
word4 = "pytho"
word5 = "drago"
if 'on' in word4 and 'on' in word5:
    print("The substring 'on' is not found in both words.")
else: 
    print("The substring 'on' is not found in both words.")

# Find the length of the text python and convert the value to float and convert it to string
length_of_python = len(word1)
length_as_float = float(length_of_python)
length_as_string = str(length_as_float)
print("Length of 'python' as a float:", length_as_float)
print("Length of 'python' as a string:", length_as_string)

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
result = 7 // 3
if result == int(2.7):
    print("The floor division of 7 by 3 is equal to the int converted value of 2.7.")
else: 
    print("The floor division of 7 by 3 is not equal to the int converted value of 2.7.")

#Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("The type of '10' is equal to the type of 10.")
else:
    print("The type of '10' is not equal to the type of 10.")

#Check if int('9.8') is equal to 10
if int(float('9.8')) == 10:
    print("int('9.8') is equal to 10.")
else:
    print("int('9.8') is not equal to 10.")

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("The pay of the person is:", pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter the number of years: "))
seconds = years * 365 * 24 * 60 * 60
print("The number of seconds a person can live is:", seconds)

#Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")