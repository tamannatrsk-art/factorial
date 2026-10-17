picnic_items = {"apples ": 5, "cups" : 2}
print("I am bringing " + str(picnic_items.get("cups" , 0)) + "cups.")
print("I am bringing" + str(picnic_items.get("eggs" , 0)) + "eggs.")
spam = {"name " : "pooka" ,"age" : "5"}
if "color" not in spam:
    spam["color"] = "black"
print(spam)
spam.setdefault("pencil" , "red")
print(spam)
spam.setdefault("color" , "White")
print(spam)
message = "It was a bright cold day in April, and the clocks were striking thirteen"
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)