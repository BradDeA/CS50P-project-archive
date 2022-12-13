# input name of fruit
fruit = input('Item: ')

# Create dictionary for fruits & calories
fruits = {
    'apple': '130',
    'avocado': '50',
    'banana': '110',
    'cantaloupe': '50',
    'grapefruit': '60',
    'grapes': '90',
    'honeydew melon': '50',
    'kiwifruit': '90',
    'lemon': '15',
    'lime': '20',
    'nectarine': '60',
    'orange': '80',
    'peach': '60',
    'pear': '100',
    'pineapple': '50',
    'plums': '70',
    'strawberries': '50',
    'sweet cherries': '100',
    'tangerine': '50',
    'watermelon': '80',
}


#function to convert to lower case & find in dictionary
def calories(str):
    f = str.lower()
    if f in fruits:
        return fruits[f]
    else:
        return ''


# output number of calories for 1 portion
print(calories(fruit))
