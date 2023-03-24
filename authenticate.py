# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True 
}

# def authenticated(fn):
#   def wrapper(*args, **kwargs):
#     if args[0]['valid']:
#         return fn(*args, **kwargs)
#   return wrapper

def authenticated(fn):
  def wrapper_func(user):
      if user['valid']:
        fn(user)
  return wrapper_func
      

@authenticated
def message_friends(user):
    print(f"The message has been sent from {user['name']}")

message_friends(user1)