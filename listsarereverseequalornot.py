# lists are reverse equal or not
 
lst1 = [5, 6, 7, 8]; lst2 = [8, 7, 6, 5]
l = []
# reversing list 2 elements
# using insert function
for i in lst2:
    l.insert(0, i)
# comparing the first list with
# reverse list if both are equal
# then return true otherwise false
if lst1 == l:
    print("True")
else:
    print("False")
