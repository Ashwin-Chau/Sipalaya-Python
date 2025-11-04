'''
Write a function that take list of string and show only string  which are start with s
'''

# def show():
#     name_list = ['sujan','manoj','suman','raj',"David","Syam"]
#     output = []
#     for i in name_list:
#         if i.lower().startswith("s"):
#             output.append(i)
    
#     print(output)

# show()




name_list = ['sujan','manoj','suman','raj',"David","Syam"]

def show(names):
    output = []
    for i in names:
        if i.lower().startswith('s'):
            output.append(i)

    print(output)

show(name_list)
