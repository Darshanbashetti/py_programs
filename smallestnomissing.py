# Given an unsorted array arr[] with both positive and negative elements, 
# the task is to find the smallest positive number missing from the array.

a= { 2, 3, -7, 6, 8, 1, -10, 15 }
for i in a:
    for j in range(1,len(a)):
        if j not in a:
            print(j)
            break
    break
