#Regular Expressions:
#re.split, re.refill, re.search, re.sub. prefix, re.replace
#regexes
"""
"""#without regex functions
email=input("Give Email Id to validate: ")

if '@' in email and "." in email:
    print("Valid")
else:
    print("invalid")  


#Syntax for Regex
#re.search(pattern, string,flags=0)
email=input("Give Email Id to validate: ").rstrip() #remove the spaces beginning and end

username,domain=email.split("@") # split the value with the keyword @
print(f'{username},{domain}')
if username and domain.endswith(".com"):
    print("Valid")
else:
    print("invalid") 