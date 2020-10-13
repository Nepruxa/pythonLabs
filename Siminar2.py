
#1
string = "zzzaabbbccc"
maxim = 0
arr = []
d = {}
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

#2
def tripleword(s):
    splitted = s.split()
    cnt = 0
    for w in splitted:
        if w.isalpha():
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True
    return False

s = "as34s sdsd 3 sdsd sdsd"
print("Task 2 : ", tripleword(s))

#3
def longest(s):
    prev = 'a'
    longest = 0
    current = 0
    for i in s:
        l = i.lower()
        if prev != l:
            if longest < current:
                longest = current
            current = 0
        current += 1
        prev = l
    return longest

s = "aaaaaasssssssszzzzzzzz"
print ("Task 3 : ", longest(s))

#4 
def bigBrother(s):
    bB = ""
    for elem in s: 
        if elem.isalpha() and elem.isupper(): 
            bB += elem
    return bB
s = "HEETEEtEEEfjskf SsdB123f??.,, U"
print ("Task 4 : ", bigBrother(s))

#5 
array = [4,4,6,4,2,2,4,6]
newArray = []
maxim = 0
d = {}
i = 0
count = 0
for elem in array:
       if d.get(elem) is not None:
           d[elem] += 1
       else: 
            d[elem] = 1
print (d)
maxim = d[max(d, key = d.get)]
print (maxim)
count = len(d)
print (count)
while count > 0:
    for elem in d:
        if d[elem] == maxim:
            i = d[elem]
            while i > 0 : 
                newArray.append(elem)
                i -=1
        maxim -= 1
count -=1
print ("Task 5 : ", newArray)