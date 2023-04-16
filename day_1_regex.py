# How to use regex python
import re  # import re module

# Here in this example we will use how to use search method
# It takes two argument : pattern and text to scan

search_result=re.search(r"^The.*Spain$","The rain in Spain")
print(search_result)
# If no match happen it will return None
# It returns the match object and match span with matched string
# Here is example output : <re.Match object; span=(0, 17), match='The rain in Spain'>
# Search method return has properties and object
# Property : 1. string property-->It will return passed string in the method
# Method :   1. span()--> it will return index where there was match
#            2. group()-->

print(f"Here is span of matched string,matched group and string {search_result.span()}, {search_result.groups()}, "
      f"{search_result.string}")
# Output of matched string
# Here is span of matched string,matched group and string (0, 17), (), The rain in Spain

# Taking another example
sr=re.search("ai","The ai is empowering ai our aiworld")
print(sr, sr.string, sr.span(), sr.group())

# Search will only return matched pattern of the string


# Next part of the coding on regex:
# here we will study search method in detail:
# search method scans the string for first match of pattern and once it finds it , stop execution and
# return re.Match object
# use it to search the entire string

# re.search(pattern, text_string, flags=0)

# it will return None if none , if string does not contain the pattern
import re
res=re.search(r"\b\w{5}\b","Jessa and Kelly")  # \w is alphanumeric regex
print(res)
print(res.span())  # return the matched span in form of tuple (0, 5)
# <re.Match object; span=(0, 5), match='Jessa'>
print(res.group()) # return matched string  Jessa

target_string="Emma is baseball player who was born on June 17"

# search for

result=re.search(r"\w{8}",target_string)
print("Matching object",result)  # <re.Match object; span=(8, 16), match='baseball'>
print("Matching word",result.group())

# why we use raw string ? As we know \ has spacial meaning , like escape sequence or escape character ,
# to avoid that we used raw string

# how to find exact substring or word
# find exact string ball

result=re.search(r"ball", target_string)
print(result)

# find the exact word surrounded by word boundary
result=re.search(r"\bball\b", target_string)
print(result)  # None because there is no word ball

# find the word player
result=re.search(r"\bplayer\b", target_string)
print(result)  # <re.Match object; span=(17, 23), match='player'>


#When to use search method:
# Ans --> when you want to find first match and possibility of pattern in long string

# when not to use:
# if you want all matched pattern then use --findall
# if you want to match at start then use re.match()
# if you want some substitution then do not use --> use re.sub(), method


# Example to search multiple pattern in  the string
result=re.search(r"(\w{8}).+(\d{2})",target_string)
print(result)
print(result.groups())  # ('baseball', '17')
print(result.group(1), result.group(2))  # 'baseball', '17'


# Multiple search using pipe operaor

result = re.findall(r"\bEmma\b|\bplayer\b|\bborn\b", target_string)
print(result)

#  ['Emma', 'player', 'born']

# for case insesnsitive use re.ignorecase

result = re.search(r"emma", target_string, re.IGNORECASE)
print("Matching word:", result.group())  # Matching word: Emma




























