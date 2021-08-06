low = 1
high = 1000

print("Plz think of a no b/w {} and {} :".format(low, high))
input("PRESS ENTER TO START THE GAME !")

guesses = 1
while True:
    print("\t PLZ GUESS b/w {} and {} ".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("MY guess is : {} ."
              " Should i guess low (l) or high (h) or"
             " i am correct (c) :::".format(guess)).casefold()
    if high_low == "h":
         low = guess + 1
    elif high_low == "l":
         high = guess - 1
    elif high_low== "c":
         print("I got that in {} guesses ".format(guesses))
         break
    else:
        print("INVALID INPUT ::")
        break

    #guesses =guesses + 1
    guesses += guesses
