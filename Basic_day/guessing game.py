import random                        #importing random module
answer1 = random.randint(1,11)       #using randint from random module
print("You can cheat from here ::::  {}".format(answer1))  #TODO:  remove this!      #todooppppppp
guess = 0
print("please guessssssss:::::: ")

while guess != answer1:
    guess = int(input())

    if guess == answer1:
        print("SAHI JAWAB $$$$$$$$$$$$$$$$")
        break
    else :
        if guess < answer1:
            print("guess higher : ")
        else:
            print("plz guess lower : ")
    # guess = int(input())
      #  if guess==answer1:
      #      print("CORRECT $$$$$")
      # else:
      #      print("INCORRECT ------ ")

    ###########################################################################################

# ###############THIS IS THE LONG CODE FOR THE SAME ########################################
# if guess < answer1:
#     print("toooo lowwwww ::::::!!!!! guess a high  ")
#     guess2 = int(input())
#     if guess2 == answer1:
#          print("YOU GUESSED IT CORRECTLY  $$$$$$")
#     else:
#          print("wrong ")
#
# elif guess > answer1:
#     print("tooooo high :::::::!!!!!!!  guess a low")
#     guess2 =int(input())
#     if guess2 == answer1:
#         print("YOU GUESSED IT CORRECTLY  $$$$$$")
#     else:
#         print("wrong ")
# else :
#     print("YOU WON @@@@@@@@@@@@@@@@")
# #########################################################################################