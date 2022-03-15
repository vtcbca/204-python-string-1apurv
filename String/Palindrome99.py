#21BCA99 - APURV JOSHI
s=input("Please Enter Any Word/Number : ")
c=s[::-1]
if s==c:
    print("Given Word/Number {} Is a Palindrome.".format(s))
else:
    print("Given Word/Number {} Is Not a Palindrome.".format(s))
