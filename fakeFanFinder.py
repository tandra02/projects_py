print('🕵🏼 Fake Fan Finder 👁️')
print('----------------------')
tvShow = input("What is your favorite tv series?\n ")

if tvShow == "Supernatural":
    print('')
    print("Oh really?!?")
    faveCharacter = input("Who is your favorite character?\n ")
    if faveCharacter == "Sam":
        print('')
        print("You got that by pure chance. ")
        he = input('Okay then, what was he? \n')  # You should ask the user what 'he' is before using it
        if he == 'Special':
            print('Hmph!\n')
        else:
            print("See! FAKE Supernatural fan!")
    else:
      print('i like him too. \n')
elif tvShow == "paw patrol":
    print("Aww, sad times")
else:
    print("Yeah, that's cool and all…")