string = str(input("String: "))

len = len(string)
id1 = string.find('1')
id2 = string.rfind('1')
stringCaps = string.capitalize()
stringUpper = string.upper()
stringLower = string.lower()
isDigits = string.isdigit()

print(len, id1, id2, stringCaps, stringLower, stringUpper, isDigits)