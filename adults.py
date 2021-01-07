list = [ 
    {
    'name': 'Ariel',
    'age': 28
    },

    {
    'name': 'Andre',
    'age': 17
    }
]

def adults(people):
    names = []

    for i in range(0, len(people)-1):
        person = people[i]
        if person['age'] >= 18:
            names.append(person['name'])
    return names        

print(adults(list))    

help
