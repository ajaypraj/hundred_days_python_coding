# Here we are going to learn regex sub method
import re

# Replace all white space with -

target="Here is simple target string"
result=re.sub(r"\s+", "-", target)
print(result)  #Here-is-simple-target-string

# How to remove all white spaces from the string
target_string = "    John   knows testing and Machine Learning        "

result=re.sub(r"\s+","", target_string)
print(result)  #JohnknowstestingandMachineLearning


# how to remove beginnning and trailing while spaces only
result=re.sub(r"^\s+|\s+$","",target_string)
print(result)  #John   knows testing and Machine Learning


target_string="John knows testing and machine learning"
result=re.sub(r"\s+","-",target_string, count=3)
print(result)  #John-knows-testing-and machine learning


# replacement function to convert upper case letter to lower case letter

def convert_to_lower(match_obj):
    if match_obj.group() is not None:
        return match_obj.group().lower()

str="Annie Loves PYTHON and MONKEY. SHE IS good girl"
res=re.sub(r"[A-Z]",convert_to_lower, str)  #annie loves python and monkey. she is good girl
print(res)

# Matching the group  of regex
def convert_upper_lower(match_obj):
    if match_obj.group(1) is not None:
        return match_obj.group(1).lower()
    if match_obj.group(2) is not None:
        return match_obj.group(2).upper()

res=re.sub(r"([A-Z])|([a-z])",convert_upper_lower,str)
print(res)   #aNNIE lOVES python AND monkey. she is GOOD GIRL



