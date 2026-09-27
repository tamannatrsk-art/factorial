birthdays = {"Alice" : " Apr 1 " , "Bob" : "Dec 12", "Carol" : "Mar 4"}
while True:
    print("Enter a name : (blank or quit )" )
    name = input("Enter a name : ")
    if name == "" :
        break

    if name in birthdays :
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print ("I do not have birthday information for " + name)
        print("What is their birthday?")
        Birthday = input("Enter Birthday date and month : ")
        birthdays[name] = Birthday
        print("Birthday database update.")