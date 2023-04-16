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

















