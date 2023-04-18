# How to split string using re.split() method
import re

# Here is general use of re.split() method syntax
# re.split(pattern, string) will split the string on occurrence of each pattern
# here is syntax for method re.split(pattern, string, maxsplit=0, flags=None)
# here maxsplit specifies  maximum number of split allowed
# flags can be re.I etc
# this method return split string in the form of list

target_string ="my name is maximus and my lucky number is 12 45 78"

# Split on white spaces

word_list=re.split(r"\s+",target_string)
print(word_list)
# ['my', 'name', 'is', 'maximus', 'and', 'my', 'lucky', 'number', 'is', '12', '45', '78']

target_string="12-45-98"
result=re.split(r"\D+", target_string, maxsplit=1)
print(result)  # ['12', '45-98']

result=re.split(r"\D+", target_string, maxsplit=2)
print(result) #['12', '45', '98']

result=re.split(r"\D+", target_string, maxsplit=3)
print(result) #['12', '45', '98']  Maxspilt specifies at most number of split  allowed

# Regex to split string with multiple deliiters
# Below example will split the string with , and - delimiter

target_string="12,45,76-12-20-53"
result=re.split(r"-|,",target_string) #['12', '45', '76', '12', '20', '53']
print(result)

# Regex to split string using five delimiters

target_string= "Pycon dot.com is website , developed by Python-developer "
result=re.split(r"[-;,.\s]\s*", target_string)
print(result)

# metacharacter [] is used for including the list of delimiter
# here it matches hyphen, semicolon, comma , dot and a space character
# It also split the string by any number space character

# Regex to split string into words with multiple word boundary delimiters
target_string="Geek for Geek is web-site for Python,JS for Web-developer community?"
result=re.split(r"[\b\W\b]+",target_string)
print(result)
# ['Geek', 'for', 'Geek', 'is', 'web', 'site', 'for', 'Python', 'JS', 'for', 'Web', 'developer', 'community', '']

# Split string by delimiter or word

text="12, and45,-and3254-and"
result=re.split(r"and|[,-]", text)
print(result)

# Keeping the limiter in result output
text="12-45-78"
result=re.split(r"\D+", text)
print(result)  #['12', '45', '78']

# As we can here in above output the delimiter is not coming to result
# Now, in other example we an print delimiter as well

result=re.split(r"(\D+)", text)
print(result)  #['12', '-', '45', '-', '78']


# How to use ignorecase flag
test_string="wkhdisUWGDSBshfs13DWJHDdkbd"
result=re.split(r"[a-z]+",test_string)
print(result)  # ['', 'UWGDSB', '13DWJHD', '']

# using the flag re.IGNORECASE flag
result=re.split(r"([a-z]+)",test_string, flags=re.IGNORECASE)
print(result)  #['', 'UWGDSB', '13DWJHD', '']

# Split a string by upper case letter
test_string ="Enna Loves Python and Machine Learning"
result=re.split(r"\s(?=[A-Z]+)", test_string)
print(result)


# re.subn(pattern, replacement_string, target_string)
# It is similar to re.sub method but it return a tuple containing two element
# 1. Modified string
# 2. Number of replacement done

target_string="Annie loves APPLE,BANANA,COCONUT ice cream"
result=re.subn(r"[A-Z]{2,}","MANGO",target_string)
print(result)  #('Annie loves MANGO,MANGO,MANGO ice cream', 3)










