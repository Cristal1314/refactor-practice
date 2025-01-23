shopping_list = ["apples", "bananas", "carrots"]
def shopping_lists(shopping_list):
    shopping_list.append("dates")
    shopping_list.remove("bananas")
for item in shopping_list:
    print(item) 