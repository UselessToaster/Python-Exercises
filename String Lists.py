### determines if a word is a palindrome ###

# reverses word
wrd = input("Give me a palindrome: ").strip()
rvs = wrd[::-1].lower()

# if the word is not equal to its reverse then it will prompt until it receives a word that is
while wrd.lower() != rvs:
    wrd = input("{} is not a palindrome! Give me a pal-in-drome! (a word spelled the same way forwards and backwards) ".format(wrd)).strip()
    rvs = wrd[::-1].lower()
else:
    print("Now THIS is a palindrome :D")