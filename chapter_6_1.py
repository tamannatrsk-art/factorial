import random

Dog = ["Leo","jack","Lucky","Shadow"]

cat_names = []
while True :
    
    name = input("Enter the name of cat " + str (len(cat_names) + 1) + "(or enter nothing to stop.):")
    if name == "":
        break
    cat_names = cat_names + [name]
print("The cat names are :",cat_names)
for i in range(len(cat_names)):
    print("Index" + str(i) + "in supplies is :"+ cat_names[i])
print("tina" in cat_names)
print("rina" not in cat_names)
name = input("Enter cat name : ")
if name not in cat_names:
    print("I don't have a cat name ",name)
else:
    print(name + " is my pet.")

size = Dog[0]
print(size)
print(Dog)

choice = random.choice(Dog)
random.shuffle(Dog)
print(choice)
print(Dog)

pets = Dog + cat_names
print("pets : ",pets)

print(pets.index("Tom"))
pets.append("Rabbit")
pets.insert(5,"Parrot")
pets.remove("Shadow")
pets.sort()
pets.sort(reverse=True)
print(pets)
pets.sort(key=str.lower)
pets.reverse()
print(pets)


Bird = ["Crow",
"Eagle",
"Moyna",
"Duck"]
print(Bird[2])
if Bird[0] == "Crow" :
    print("Crow id the 1st item.")
else:
    print("The 1st item is not Crow")

print("Ask a yes or no question : ")
input(">")
print(Bird[random.randint(0, len(Bird) - 1)])
