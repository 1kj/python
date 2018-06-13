s = input("Type the string to be reversed:")
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
#s = "1234567"
print (reverse(s))