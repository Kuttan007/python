""" Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir'] """

#!/usr/bin python3
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=list1[0]+list2[0]
list4=list1[0]+list2[1]
list5=list1[1]+list2[0]
list6=list1[1]+list2[1]
print([list3,list4,list5,list6])
