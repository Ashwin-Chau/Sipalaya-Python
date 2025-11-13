'''
module : file that contain python code(variable,function,class etc) that can be reuse in other python program

#main purpose:
code reuability
code organize
fast debug
maintenance


type of module :
#built in module : pre-coded modules that come with Python itself — you don’t need to install anything.
#user define module : modules you create yourself — basically, your own .py files with reusable functions or classes.
#external module : modules developed by others and available on the Python Package Index (PyPI). You must install them using pip.


scripts : a Python file (.py) meant to be run directly — it performs some action or task.
module : a Python file (.py) that contains code you want to reuse — functions, classes, variables, etc.

package : (a folder that contains multiple modules and a special file named __init__.py.) 
        collection of module (folder1 ----> __init__.py : to say it is package
                                      ---->module.py
                                      ----> module1.py  
                                      ----> module2.py  

library : (a collection of packages and modules designed to solve specific kinds of problems.) 
             collection of package is library (folder --->package1
                                                      --->package2
                                                      --->package3)
'''

# import random
# print(random.choice([1,2,3]))
# print(random.choices([1,2,3],k=2))


# import keyword
# print(keyword.kwlist)


# import calendar
# # print(calendar.month(2025,11))
# print(calendar.calendar(2025))


# from datetime import datetime
# print(datetime.now())
# print(datetime.now().year)
# print(datetime.now().date())
# print(datetime.now().time())


# import math

# c=math.sqrt(36)
# c=math.factorial(5)
# #1.00001 1.2 1.3 ----- 1.9
# c=math.floor(3.999)
# c=math.ceil(3.0001)
# c=round(3.267)
# print(c)
# c=round(3.267,2)
# print(c)
# var=math.radians(30)
# c=math.sin(var)
# print(c)


# from math import sqrt
# c=sqrt(36)
# print(c)


# from math import sqrt,factorial
# c=sqrt(36)
# d=factorial(5)
# print(c)
# print(d)


# import math
# print(dir(math))


# from math import * # * make performance slow
# c=sqrt(36)
# print(c)


# from math import sqrt as a #used when (name is hard / two module have same name)
# c=a(36)
# print(c)





# user defined

# import file
# print(file.names)
# print(file.show(2, 3))




# from file import names,show
# print(names)
# print(show(2, 3))





# from file import * #use * when all the things needed of that file
# print(names)
# print(show(2, 3))