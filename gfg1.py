def swap(list):
    temp = list[0]
    list[0]=list[-1]
    list[-1]=temp
    return list

def swap2(list):
    list[-1], list[0]= list[0], list[-1]
    return list

def swap3(list):
    touple = list [-1], list[0]
    list [0], list[-1] = touple
    return list

def swap4(list):
    list = list[-1:] + list [1:-1] + list [:1]
    return list

newList = [12, 35, 9, 56, 24]
print(newList)
print(swap4(newList))