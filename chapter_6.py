spam = ["cat", " bat" , "rat" , " elephant"]
another_list = [["fish","hen"],[10,20,30,40,50]]
print(spam[0])
print(spam[1])
print(spam[2])
print("The" + spam[1] + "are the " + spam[0])
for i in range(8):  # try excpet
    try:
        if i >3:
            raise IndexError("Index is not here.")
            print(spam[i])
    except IndexError as e :
        print(e)


print(another_list[0])
print(another_list[0][1])
print(another_list[1][4])

for j in range(6): # try excepct
    try:
        if j >2:
            raise IndexError("Index is not here.")
            print(another_list[j])
    except IndexError as e :
        print(e)

del spam[2] # list delete
print(spam)
print(len(spam)) # list len
spam[-1] = 12345 # list replace
print(spam)




print("Enter the of cat 1 : ")
cat_name_1 = input()
print("Enter the of cat 2 : ")
cat_name_2 = input()
print("Enter the of cat 3 : ")
cat_name_3 = input()
print("Enter the of cat 4 : ")
cat_name_4 = input()
print("The cat names are : ")
print(cat_name_1 + ' ' + cat_name_2 + ' '+ cat_name_3 + ' ' + cat_name_4 +' ')



for i in range(4):
print(i)
