inpu  = input("Enter a charcter ")
if ((inpu =='a' or inpu =='A') or (inpu =='e' or inpu == 'E') or (inpu == 'i' or inpu=='I') or (inpu== 'o' or inpu=='O') or (inpu == 'u' or inpu=='U')):
     print("The charctr is vowel ")
elif((inpu >='a' and inpu<='z')  or(inpu>='A') or inpu<='Z'):
    print("The character is consonant")
else:
    print("Neither consonant nor vowel")