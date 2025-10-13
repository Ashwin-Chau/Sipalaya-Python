'''
Given a dictionary:
my_details = {
    'name':'sujan',
    'grade': 0,
    'address':'ktm',
    'hobbies':{
        'sports':'running',
        'game':'pubg',
        'novel':'xyz',
        'anime':'one piece',
    },
    'email':'sujan@gmail.com'
}
Change the value of 'novel' key from 'xyz' to 'Harry Potter'
'''

my_details = {
    'name':'sujan',
    'grade': 0,
    'address':'ktm',
    'hobbies':{
        'sports':'running',
        'game':'pubg',
        'novel':'xyz',
        'anime':'one piece',
    },
    'email':'sujan@gmail.com'
} 

my_details['hobbies']['novel']="Harry Potter"

print(my_details)