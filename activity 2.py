set1={1,1,1,2,2,3,3,3,4,5,5,6}
print("set1 is",set1)

set2={2,4,9,5,8,3}
print("set2 is",set2)

set2.add(10)
print("Updated set2 is",set2)

#defference
print("defference of set1 and set2",set1.difference(set2))
print("defference of set2 and set1",set2.difference(set1))

#symmentric defference
print("symmentric defference of set1 and set2 is",set1.symmetric_difference(set2))
print("symmentric defference of set2 and set1 is",set2.symmetric_difference(set1))

