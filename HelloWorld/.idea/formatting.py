#RIGHT ALLIGN
for i in range(1,13):
  # **********clean {0:col}
    print("number {0:2} square is {1:4} and cubed is {2:7}".format(i,i**2,i**3))
print()

#LEFT ALLIGN  <
for i in range(1,13):
    print("number {0:2} square is {1:<3} and cubed is  {2:<4}".format(i,i**2,i**3))

#center ALLIGN  ^
for i in range(1,13):
    print("number {0:2} square is {1:^3} and cubed is  {2:^4}".format(i,i**2,i**3))


    print()

    print("value of pie is {0:12} ".format(22/7))
    print("value of pie is {0:12f} ".format(22/7))


    ##F STRING
    name="ram"
    age=input("Enter age: ")
    print("nameage" + name + age )
