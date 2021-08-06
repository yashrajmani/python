choice= "-"
while True:
    if choice == "0":
        break
    elif choice in "1234":
        print("You have chosen {}".format(choice))
    else:
        print("PLEASE CHOOSE : ")
        print("1:\t Learn Python")
        print("2: \t Learn Java")
        print("3: \t Go swim")
        print("4: \t Have dinner")
        print("0: \t EXIT ! ")
    choice = input()


