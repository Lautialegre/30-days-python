firstname = "lautaro"
lastname = "alegre"
fullname = "lautaro alegre"
country = "argentina"
city = "buenos aires"
age = 21 
year = 2026
is_married = False 
is_true = True
is_light_on = True
firstname, lastname, fullname, country, city, age, year, is_married, is_true, is_light_on = "lautaro", "alegre", "lautaro alegre", "argentina", "buenos aires", 21, 2026, False, True, True

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(firstname))
print(len(lastname))

number_one = 5
number_two = 4 
sum = number_one + number_two
subtraction = number_one - number_two
multiplication = number_one * number_two
division = number_one / number_two
modulus = number_one % number_two
potency = number_one ** number_two
floor_division = number_one // number_two

#Radius of a circle 
r = 30 #meters
pi = 3.14
circle = pi * r **2 
perimeter = 2 * pi * r

print("Area of the circle:", circle)
print("Perimeter of the circle:", perimeter)

#radius variable 
r = int(input("Enter the radius of the circle: "))
pi = 3.14
circle = pi * r **2 
perimeter = 2 * pi * r
print("Area of the circle:", circle)
print("Perimeter of the circle:", perimeter)

user_firstname = input("Enter your first name: ")
user_lastname = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))