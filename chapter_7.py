my_cats = {"size" : "fat", "color" : "gray" , "age" : 17}
my_Dogs = {"size" : "fat", "color" : "gray" , "age" : 17}


spam = {12345 : "Luggage Combination " , 42 : "The Answer"}
print(my_cats["size"])
print("My cat has " +my_cats["color"] +" fur")
print(spam[12345],spam[42])
print("Spam == My cats : ",spam == my_cats)
print("My_cats = My Dogs : ",my_cats == my_Dogs)

try :
    print(spam["color"])
except KeyError:
    print ("The key 'color' does not exist.")

for v in my_cats.values():
    print(v)
print("color" in my_cats.keys())
print("Height" not in my_cats.keys())
for i in spam.items():
    print(i)
print(spam.keys())
print(list(spam.keys()))

for k,v in spam.items():
    print("Key : " + str(k) + "Value : " + str(v))