       #012345678901234
parrot="Norwegain Blue"
print(parrot[0:2])  #No  //// zero one but ************not upper limit**************)
print(parrot[:2])  #No  //// by default zero one but ************not upper limit**************)

print(parrot[3:6])  # weg  //// three four five but ************not upper limit**************)
print(parrot[10:])  #blue //// from 10to end**************)
print(parrot[:])  #starting to end **************

#negative numbers slicing ***********
print(parrot[-4:-2])       #from back index counting is done still upper limit not included

#step slicing\\\\ print second term
print(parrot[0:6:2]) #nre
print(parrot[0:6:3]) #nw //// third term


 #seperators slicing
 #    0123456789
num= "3,12,4546 7;9-0"
print(num[1::4])    # seperator at 1 ,4th term everytime (,4 -)


#backwards  slicing
letter="abcdefghijklmnopqrstuvwxyz"
back=letter[25:0:-1]       # still upper limit not included        (z to b )
backall=letter[25::-1]       # till the begining                   (z to a)
backall2=letter[::-1]       # from end till the begining           (z to a) **IDIOM: FOR REVERSING THE SEQUENCE****
print(back)
print(backall)
print(backall2)

task1=letter[16:13:-1]     #qpo
print(task1)

task2=letter[4::-1]   #edcba
print(task2)

task3=letter[25:17:-1]   #last 8 in reverse
#same as [:-9:-1]   from end till upper limit not included in reverse ****
print(task3)

print(letter[-4:])    #wxyz
print(letter[-1:])      #z
print(letter[:1]) #from begining till upper limit not included  #(a)     ***IDIOM: first letter of sequence *****


