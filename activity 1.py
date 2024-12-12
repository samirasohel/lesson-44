tup1=()

#tuple with integer
tup2=(2,5,1,7)
print("tuple 2 is",tup2)

#tuple with defferent datatypes
tup3=("samira",2,35.6)

print("name of the student is",tup3[0])

print("tuple 3 is",tup3)

#nested tuple

tup4=("hello",[1,2,3],[4,5,6],[7,8,9])
print(tup4[0][1])
print(tup4[1][2])
print(tup4[2][1])

#slicing
print("sliced tuple is",tup2[1:3])

tup5=('c','o','d','i','n','g','a','l')
for tup in tup5:
    print("Hello",tup)