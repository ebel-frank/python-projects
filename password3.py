print("A valid Password")
print("""-Minimum length is 5
-Maximum length is 10
-Should contain aleast one number
-Should contain at least one special character(such as &,+,@,$,#,%,etc.)
-should not contain spaces.
""")
def Length():
    print("minimum length of 5, maximum length 10")
    trial()
def Numb():
    print("Should contain aleast one number")
    trial()
def Special():
    print("Should contain at least one special character")
    trial()
def Space():
    print("should not contain spaces")
    trial()
def trial():
    ans = input("press enter to try again or type 'quit' to exit program: ")
    ans = ans.lower()
    if ans == 'quit':
    	raise SystemExit()
    else:
	    check()
def check():
    passw = input("Enter a valid password: ")
    if len(passw)<5 or len(passw)>10:
        Length()
    else:
        pass
    if '1' in passw or '2' in passw or \
       '3' in passw or '4' in passw or \
       '5' in passw or '6' in passw or \
       '7' in passw or '8' in passw or \
       '9' in passw or '0' in passw:
        pass
    else:
        Numb()
    if '&' in passw or '+' in passw or \
       '@' in passw or '$' in passw or \
       '#' in passw or '%' in passw or \
       '^' in passw or '!' in passw or \
       '(' in passw or ')' in passw:
        pass
    else:
        Special()
    if " " in passw:
        Space()
    else:
        pass
check()
print("Thank You For Inputing a Valid Password")
input()
