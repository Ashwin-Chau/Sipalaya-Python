'''
Task: Filter names starting with 'S' or 's' (case-insensitive) and store them in a new list.
input=['sujan','manoj','suman','raj',"David","Syam"]
expected_output=["sujan",'suman',"syam"]
'''

name_list = ['sujan','manoj','suman','raj',"David","Syam"]

output = []

for name in name_list:
    if name.lower().startswith('s'):
        output.append(name.lower())

print(output)