
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
def task5(array):
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
    maxim = d[max(d, key = d.get)]
    count = len(d)
    while count >= 0:
        for elem in d:
            if d[elem] == maxim:
                i = d[elem]
                while i > 0 : 
                    newArray.append(elem)
                    i -=1
        maxim -= 1
        count -=1
    return newArray
array = [4,4,6,4,2,2,4,6,6,6,6]
print ("Task 5 : ", task5(array))

#6
def closest(number,arr):
    arr = sorted (arr)
    previous = arr[0]
    for elem in arr:
        if elem >= number:
            return previous
        else: previous = elem
f = [[1,4,2,5], 3]
print ("Task 6 : ", closest(f[1], f[0]))

#7
import numpy as np
n = 8
x = 0
y = 0
field = np.zeros((n,n), dtype=np.int64)
for i in range(n-1,-1,-1):
    for j in range(n):
        if i == n-1:
            field[i][j] = 1
            continue
        if j - 1 >= 0:
            field[i][j] += field[i+1][j-1]
        if j + 1 < n:
            field[i][j] += field[i+1][j+1]
def rec(x, y):
    if y >= n-1:
        return 1
    left = rec(x-1, y+1) if x - 1 >= 0 else 0
    right = rec(x+1, y+1) if x+1 < n else 0
    return left + right

print("Task 7 : ",rec(0, 0))