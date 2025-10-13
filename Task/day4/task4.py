'''
Given the dictionary person = {'name': 'sujan', 'age': 23, 'city': 'Kathmandu'}, 
add a new key-value pair 'job': 'Developer' to the dictionary. 
Then update the value of the 'name' key to 'Ram Bahadur' and 'age' to 29
'''

person = {
    'name':'sujan',
    'age':23,
    'city':'kathmandu'
}

person['job']='Developer'

person['name']='Ram Bahadur'
person['age']=29


print(person.items())