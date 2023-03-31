# Ceaser Ciphher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

massage = input('Enter massage: ')
LETTERS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blank string so that the
    #previous iteration's value for translated is cleared.
    translated = ''

    # The rest of the program is the same as the original Ceaser program:

    # run the encryption/decryption code on each symbol in the massage
    for symbol in massage:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) #get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add thhe symbol without encrypting/decrypting
            translated = translated + symbol

    # display the current key being tested, along with its decyption
    print('key #%s: %s' % (key, translated))

    
    
