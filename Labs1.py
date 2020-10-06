#1
arr1 = [1,2,3,4,5,6]
print ("Task 1: ", arr1[0], arr1[2], arr1[len(arr1)-2])

#2
arr2 = [2,2,2,2,2]
N = 5
if len(arr2) >= N:
    print("Task 2: ", arr2[N-1] ** N)
else:
    print ("Task 2: ", "-1")

#3
string = "сбербанк банк"
isFirstFlag = True
symbolInd = 0
symb = "б"
for elem in string : 
    if string[symbolInd] == symb:
        if isFirstFlag == False:
            print ("Task 3: ", symbolInd)
            break   
        isFirstFlag = False
        
    symbolInd +=1


#4
numb = 0
zc = 0
safe = len(str(numb))
while (numb % 10) == 0:
    if zc == safe:
        break
    zc +=1
    numb = numb / 10
print ("Task 4: ", zc)

#5
str1 = "qwe"
print("Task 5: ", str1[::-1])

#6
arr3 = [2,1,1,1,1,1,1]
flag1 = True
for elem in arr3:
    if elem != arr3[0]:
        flag1 = False
print ("Task 6: ", flag1)

#7
import re
password = "12345ghH12312313sdsa"
if re.search('^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{16,}$', password) is not None:
    print ("Task 7: ", True)
else:
    print ("Task 7: ", False)

#8
arr4 = ([[2,3], [4,5], 5])
resArr = []
for elem in arr4:
    if type(elem) == list:
        resArr.extend(elem)
    else:
        resArr.append(elem)
print ("Task 8: ", resArr)

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