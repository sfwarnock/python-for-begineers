list1 = [1,2,3,10,9]

list2 = [4,6,10,8]

for word in list1:
    if word not in list2:
        list2.append(word)
    if word in list2:
        continue
list2.sort()

print list2