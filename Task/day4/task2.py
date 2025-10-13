# Get day name from user number input (1-7), where 1 = Sunday, 2 = Monday, ..., 7 = Saturday.

weeks={
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thrusday",
    6:"Friday",
    7:"Saturday"
}

user=int(input("Enter a number between 1 to 7 where 1 = Sunday, 2 = Monday, ..., 7 = Saturday : "))
v=weeks.get(user,"please enter a number between 1 to 7 only")

print(v)