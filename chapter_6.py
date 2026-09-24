spam = ["cat", " bat" , "rat" , " elephant"]
another_list = [["fish","hen"],[10,20,30,40,50]]
print(spam[0])
print(spam[1])
print(spam[2])
print("The" + spam[1] + "are the " + spam[0])
for i in range(8):
    try:
        if i >3:
            raise IndexError("Index is not here.")
            print(spam[i])
    except IndexError as e :
        print(e)


print(another_list[0])
print(another_list[0][1])
print(another_list[1][4])

for j in range(6):
    try:
        if j >2:
            raise IndexError("Index is not here.")
            print(another_list[j])
    except IndexError as e :
        print(e)

del spam[2]
print(spam)
