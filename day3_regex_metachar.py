# Python regex group pattern helps us to capture different type of groups from string
# For example, capturing email id and phonenumber,  using regex from string
# ((\w)(\s\d)) : will capture three groups 1. (\w)  2. (\s\d) 3. ((\w)(\s\d))
import re
target_string = "Price of MANGO ice cream is 50"
result=re.search(r"(\b[A-Z]+\b).+(\b\d+)",target_string)  # Here \b is word boundary
# It will capture two groups , no of groups captured=open parenthesis from left to right
# print(result)
# print(result.groups()) #('MANGO', '50')
# print(result.group(1))  # MANGO
# print(result.group(2))  # 50
# print(result.group(0))  # MANGO ice cream is 50
# Regex capture group multiple times
target_string="The price of ice-creams PINEAPPLE 20 MANGO 30 CHOCOLATE 50"
regex_pattern=re.compile(r"(\b[A-Z]+\b).(\b\d+\b)")
for matched in regex_pattern.finditer(target_string):
    print(matched.group(1), matched.group(2) )  #PINEAPPLE 20
    print(matched.group(1,2))  #('PINEAPPLE', '20')

# Regex metacharcaters: how to use operators using in python"
"""
. --> . matches to any character except new line
* --> zero or more occurrence
+ --> one or more
? --> Atmost one (Zero or 1 )
[] --> used to match the set of character
() --> for group capturing
| --> logical or
\ --> for escape sequence lets say if matching speacial charcter . or ? is required then it should be used as \. or \?
^ --> match at the beginning of the string
$ --> matches the end of string com$ will match string ending with com 
"""

# Use case of metacharcter
target_string="Megha is recruitment \n consultant"
result=re.search(r".",target_string)  # It will match a single character
print(result.group())  #M

# As we know, dot does not matches to \n , lets use a flag to match \n
result=re.search(r".+", target_string, re.S)
print(result.group())
#Megha is recruitment
# consultant

# How to match at the beginning of string
str1="Emma is Python developer and her salary is 5000$ \nEmma also knows AI and ML"
result=re.findall(r"^\w{4}",str1)
print(result)  #['Emma']

# For multiline matching use the flag re.M
result=re.findall(r"^\w{4}",str1, re.M)
print(result)  #['Emma', 'Emma']

# How to match at the end of string using $ metacharacter

result=re.search(r"\w{2}$", str1)
print(result.group())  #ML
