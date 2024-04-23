def swap(list, pos1, pos2):
    temp = list[pos1]
    list[pos1]=list[pos2]
    list[pos2]=temp
    return list

def swap2(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def swap3(list, pos1, pos2):
    for i, x in enumerate(list):
        if i == pos1:
            num1=x
        if i == pos2:
            num2=x
    list[pos2]= num1
    list[pos1]=num2
    return list

list = [1,2,3,4,5,6]
print(list)
swap2(list, 1, 4)
print(list)