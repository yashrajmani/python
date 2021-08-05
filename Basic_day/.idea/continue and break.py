shop_list=["Milk ","Sugar","Jam", "Spammm", "Butter ","Chesse"]
for item in shop_list:
    if item == "Spammm":
        continue         #########SKIP THIS SPAMMMM ############
    print("buy "+ item )

print()

shop_list=["Milk ","Sugar","Jam", "Spammm", "Butter "]
for item in shop_list:
    if item == "Spammm":
        break        #########not runs after targeting SPAMMMM ############
    print("buy "+ item )

print()
########################## BREAK IS IMP #############################
print("WE ARE SEARHING SPAMMMMMM ")
shop_list=["Milk ","Sugar","Jam", "Spam", "Butter "]
found_at = None      #None is used to assign a null or 0 value
item_to_find = input("plz enter what uou need to find ")

for index in range(len(shop_list)):
    if shop_list[index]==item_to_find:
        found_at=index
        break       ###########we found the spamm plz stop searching from now ################
if found_at is not None:
 print("{} is found at :: {}  ".format(item_to_find,found_at))
else:
 print("NOT FOUND  ::::{} ".format(item_to_find))

#############################################################################################################