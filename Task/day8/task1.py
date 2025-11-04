# l = [4,1,3,1,5,8,7,6]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
    


# print(sec_largest)



v=[4,1,3,1,5,8,7,6,10]


for i in range(len(v)):
    for j in range(i+1,len(v)):
        if v[i] > v[j]:
            v[i],v[j] = v[j],v[i]

print(v[-2])
        
            