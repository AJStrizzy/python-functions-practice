
test = [4,3,6,8,9]

def tripler(array):
    result = []

    for i in range(len(array)):
        num = array[i]
        multiple = num * 3
        result.append(multiple)
    return result

print(tripler(test))        
