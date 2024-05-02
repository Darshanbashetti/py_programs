# a=[]
# middle=0
# n=int(input("Enter number of elements : "))
# for i in range(0,n):
#     a.append(int(input()))

# for i in range(0,n):
#     for j in range(i+1,n):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# if len(a)%2!=0:
#     middle=((a[n])/2)+0.5
# else:
#     pass

# print(middle)
# print(a)


nums1 = []
nums2 = []
m = int(input("Enter number of elements in nums1: "))
for i in range(m):
    nums1.append(int(input("Enter element for nums1: ")))
n = int(input("Enter number of elements in nums2: "))
for i in range(n):
    nums2.append(int(input("Enter element for nums2: ")))
merged = []
i = j = 0
while i < m and j < n:
    if nums1[i] < nums2[j]:
        merged.append(nums1[i])
        i += 1
    else:
        merged.append(nums2[j])
        j += 1
while i < m:
    merged.append(nums1[i])
    i += 1
while j < n:
    merged.append(nums2[j])
    j += 1
total_length = m + n
if total_length % 2 != 0:
    median = merged[total_length // 2]
else:
    median = (merged[total_length // 2 - 1] + merged[total_length // 2]) / 2

print("Median:", median)