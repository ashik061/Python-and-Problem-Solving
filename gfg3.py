from operator import length_hint

def countList(lst):
    
    if not lst:
        return 0
    lst.pop()
    return 1 + countList(lst)

lst = [10,20,30,40]

count=0
for i in lst:
    count +=1


print(lst)
print(len(lst))
print(count)
print(length_hint(lst))

length = sum(1 for i in lst)
print(length)

print(countList(lst.copy()))
print(lst)
