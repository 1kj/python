s = input("Type the string to be reversed:")
def reverse(s):
	if s == "":
		print ("Error! Input cannot be blank")
	else:
		str = ""
		for i in s:
			str = i + str
		return str
#s = "1234567"
print (reverse(s))