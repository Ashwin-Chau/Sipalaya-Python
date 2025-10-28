# Write a Python program to sort (ascending and descending) a dictionary by key value.


my_dict = {
    "name":"ashwin",
    "age":22,
    "address":"chitwan"
}

asec_sort_keys = sorted(my_dict.items())

desc_sort_keys = sorted(my_dict.items(), reverse=True)

print(asec_sort_keys)
print(desc_sort_keys)