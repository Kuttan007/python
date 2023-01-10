""" Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

Given:

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

Expected output:

['My', 'name', 'is', 'Kelly'] """

#!/usr/bin python3
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=list1[0]+list2[0]
list4=list1[1]+list2[1]
list5=list1[2]+list2[2]
list6=list1[3]+list2[3]
print([list3,list4,list5,list6])
