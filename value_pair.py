cat = {
    'color': 'orange',
    'age': 20
}
dog = {
    'color': 'brown',
    'age': 15
}

def value_pair(obj1, obj2, key):
    val1 = obj1[key]
    val2 = obj2[key]
    arr = [val1, val2]

    return arr

print(value_pair(cat, dog, 'color'))    