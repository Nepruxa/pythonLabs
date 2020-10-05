#1
arr1 = [1,2,3,4,5,6]
print ("Task 1: ", arr1[0], arr1[2], arr1[len(arr1)-2])

#2
arr2 = [1,2,3,4,5]
N = 2
if N <= len(arr2):
    print("Task 2: ", arr2[N-1]**arr2[N-1])
else:
    print ("Task 2: ", "-1")

#3
string = "сбербанк банк"
symb = "б"
print ("Task 3: ", string.rfind(symb))

#4
numb = 10111011100
zc = 0
while (numb % 10) == 0:
    zc +=1
    numb = numb / 10
print ("Task 4: ", zc)

#5
str1 = "qwe"
print ("Task 5: ", str1[::-1])

#6
arr3 = [2,1,1,1,1,1,1]
flag1 = True
for elem in arr3:
    if elem != arr3[0]:
        flag1 = False
print ("Task 6: ", flag1)

#7
password = "123456789123547Hh"
if 16 > len(password) or password.upper() == password or password.lower() == password:
    print ("Task 7: ", False)
else:
    print ("Task 7: ", True)

#8
import numpy as np
arr4 = np.array ([[2,3], [4,5]])
print ("Task 8: ", arr4.flatten())

#9
d = {'q': 1.1, 'w' : 0.2, 'e' : 3.7, 'r' : 3.7}
print ("Task 9: ", max (d, key = d.get))


#10 
arr5 = [1,1,2,3,4,4,5,6,7,7]
resArr = []
for elem in arr5:
    if arr5.count(elem) > 1:
        resArr.append(elem)
print ("Task 10: ", resArr)