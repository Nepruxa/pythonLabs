
#1
string = "zzzaabbbccc"
maxim = 0
arr = []
for elem in string:
    if elem.isalpha():
       if d.get(elem) is not None:
           d[elem] += 1
       else: 
            d[elem] = 1
maxim = max(d, key = d.get)
for elem in d: 
    if d[elem] == d[maxim]:
        arr.append(elem)
arr.sort()
print ("Task 1 : ", arr[0])

