print("FOR LOOPS \n")

quote = "Already,I have been There, Now coding now CODING with all Capital "
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)
    else :
        print("@")


############   RANGE    #############
print("range ")
for i in range(1,20):   #upper limit not included
    print("value of i is now : {0}".format(i))
print()

for i in range(5):   #0 to 4
    print("value of i is now : {0}".format(i))
####### LAMBA CODE FOR RANGE ####################################
print("Lamba code")
for i in range(0,100):
    if (i%7)== 0:
        print("{} is divisible by 7 ".format(i))
######## Chota Code for range $ ################################
print("chota code")
for i in  range(0,101,7):
    print(i)
##################################################################3