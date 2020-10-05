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
string = "сбербанк"
symb = "б"
si = 0
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
print ("Task 4: ", str1[::-1])

#6
arr3 = [2,1,1,1,1,1,1]
flag1 = True
for elem in arr3:
    if elem != arr3[0]:
        flag1 = False
print ("Task 4: ", flag1)