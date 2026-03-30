string1="Thirty"
string2="Days"
string3="Of"
string4="Python"    
concatenated_string = string1 + " " + string2 + " " + string3 + " " + string4
print(concatenated_string)

string5 = "Coding"
string6 = "For"
string7 = "All"
concatenated_string2 = string5 + " " + string6 + " " + string7
print(concatenated_string2)

company = "Coding For All"
print(len(company))
print(company.upper())
print(company.lower())

company.capitalize() # capitalizes the first letter of the string and makes the rest of the letters lowercase
company.title() # capitalizes the first letter of each word in the string
company.swapcase() # swaps the case of each letter in the string

print(company[0:6]) # prints the first 6 characters of the string


print(company.index("Coding")) # returns the index of the first occurrence of the substring "Coding"

company.replace("Coding", "Python") # replaces the substring "Coding" with "Python" in the string
company.replace("Python for Everyone", "Python for All") # replaces the substring "Python for Everyone" with "Python for All" in the string
print(company.split()) # splits the string into a list of words
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")) # splits the string into a list of company names

print(company[0]) # The first caracter of the string is "C"
print(company[13]) # The last index is 13 because the string has 14 characters (index starts at 0)
print(company[10]) # The character at index 10 is "space " because there is a space between "For" and "All"

company2 = "Python For Everyone"
letterp = company2[0] # The first character of the string is "P"
letterf = company2[7] # The character at index 7 is "F"
lettere = company2[11] # The character at index 11 is "E"
acronimo = letterp + letterf + lettere # The acronym is "PFE"
print(acronimo)

company3 = "Coding For All"
letterc = company3[0] # The first character of the string is "C"
letterf = company3[7] # The character at index 7 is "F"
lettera = company3[11] # The character at index 11 is "A"
acronimo2 = letterc + letterf + lettera # The acronym is "CFA"
print(acronimo2)

print(company.index("C")) # The index of the first occurrence of "C" is 0
print(company.index("F")) # The index of the first occurrence of "F" is 7
print(company.index("A")) # The index of the first occurrence of "A" is 11

company4 = "Coding For All People"
print(company4.rfind("l")) # The index of the last occurrence of "l" is 19

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because")) # The index of the first occurrence of "because" is 31
print(sentence.rindex("because")) # The index of the last occurrence of "because" is 47
print(sentence[31:54]) # The phrase 'because because because' is located between index 31 and 54
print(sentence.find("because")) # The index of the first occurrence of "because" is 31

# Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding")) # Yes, it does start with "Coding"
# Does 'Coding For All' end with a substring coding?
print(company.endswith("coding")) # No, it does not end with "coding" because of case sensitivity

company5 = "   Coding For All      "
print(company5.strip()) # The strip() method removes any leading and trailing whitespace from the string

company6 ="30DaysOfPython"
company7 = "thirty_days_of_python"
print(company6.isidentifier()) # its False because it starts with a number and contains uppercase letters
print(company7.isidentifier()) # its True because it follows the identifier rules
# The isidentifier() method checks if the string is a valid identifier in Python. 
# An identifier must start with a letter 
# (a-z or A-Z) or an underscore (_) and can be followed by letters, digits (0-9), or underscores. 
# It cannot contain spaces or special characters.

list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(list1)) # The join() method is used to concatenate the elements of a list into a single string, with a specified separator between each element.

var1 ="I am enjoying this challenge"
var2 ="I just wonder what is next"
print(var1,"\n",var2)
