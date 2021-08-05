name = input("PLZ ENTER NAME : ")
age = int(input("PLZ ENTER AGE : {0} sir ::::".format(name)))
print(name)
print()
print(age)

if age>=18:
    print("voter")
    print("yes you are ")
elif age==16:
     print("in other country")
else:
    print("plz come back in{0} years   ".format(18-age))
