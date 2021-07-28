# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    # code here
    def wrapper_func(*args, **kwargs):
        user = args[0]
        if user['valid']:
            result = fn(*args, **kwargs)
            return result
        else:
            print(f'User ({user["name"]}) are not allowed to perform this action')

    return wrapper_func


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)