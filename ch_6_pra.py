def comma_code(spam):
    if len(spam) == 0:
        return " "
    elif len(spam) == 1:
        return spam[0]
    else:
        return ", ".join(spam[:-1]) + ",and " + spam[-1]


spam = ["apples", "bananas", "tofu", "cats"]
print(comma_code(spam))
print(comma_code([]))
print(comma_code(["apple"]))
print(comma_code(["apple", "mango"]))