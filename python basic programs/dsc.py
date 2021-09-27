charac = input("Enter a character : ")
if ((charac >= 'a' and  charac<='z')or (charac >='A' and charac<='Z')):
    print("The input is a character ")

elif (charac >='0' and charac<='9'):
    print("The input is a digit")

else:
    print("The character is a special character")
    