cat = {
    'color': 'orange',
    'age': 20
}

def does_key_exist(obj, key):
    if obj[key]:
        return True
    elif not obj[key]:
        return False    

print(does_key_exist(cat, 'age')) 

