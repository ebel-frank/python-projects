print ("Hello, my name is Tyler.")
print ("What is your name?")
myName = input()
tim = len(myName)
while myName:
    if tim == 8:
        print ("Your name is kinda long\n")
        break
    elif tim > 8:
        print ("I asked for your name, not your generation's names \ncan you please type in a name that i can understand>")
        myNAME = input()
        myName = myNAME
        tim = len(myName)
        if tim > 8:
            print ("You are an unserious human being \nJust for the record, you are STUBBORN \nsince this is the crazy name you wanna use, then so be it.")
            break
        else:
            print ("Mtchewww, I thought you will not have sense.")

    else:
        break

myName = myName.capitalize();    
print ("It's nice to meet you, " + myName)
print ("Are you a girl or a boy?")
ref = input('(g/b): ')
reff = ref[0].lower()
rer = 'fuck you'
if reff == 'g':
    print ("Hmmmm. I like girls")
    print ("Do you have a boyfriend?")
    led = input('(y/n): ')
    led = led[0]
    if led == 'y':
        mit = input ("Hmmmm, How old are you that you have a boyfriend?: ")
        print ("So because you are " + mit + " you now think that you are big enough ahbi!!! \n \nOk ohh, better break up with that boy you call your boyfriend")
        print ("\nMy Dear, my name is Tyler and you should know by now, AM SINGLE AND SEARCHING \nI know its kinda weird to date a laptop that's why I \
have a representative Frank Ebeledike, \nHe is also single and searching. \nSo Please talk to him, He will guide you through the details.\n \nHave a good day " + myName)
    elif led == 'n':
        print("Wow, that's nice ohh\n")
        print ("My Dear, my name is Tyler and you should know by now, AM SINGLE AND SEARCHING \nI know its kinda weird to love a laptop that's why I \
have a representative Frank Ebeledike, \nHe is also single and searching. \nSo Please talk to him, He will guide you through the details.\n \nHave a good day " + myName)

elif reff == 'b':
    print ("mtchewww, I hate boys")
    print ("\nkindly leave me alone cos am masculine. If there is a girl nearby,\ntell her to come, that I want to speak to her!!!")
elif rer in ref:
    print("Thunder fire you there!!!" "\n"+ rer + " too")
else:
    print("Please be reasonable for once in your life time.")

input()
