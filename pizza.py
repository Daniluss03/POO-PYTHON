# POO-PYTHON
def make_pizza(size,*toopings):
    """summariz the pizza we are about tomake"""
    print("\nMaking a  "+str (size)+"  pizza size ,making the pizza with the following toppings:")
    for topping in toopings:
        print('-'+ topping)

make_pizza(12,'peperoni','queso','mayonesa')       


def build_profile(first,last,**user_info):
    """Build a dictinary containing everything weknow about a user"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

user_profile=build_profile('albert','einstein',
                             location='princenton',
                             field='pyhsics')

print(user_profile)
