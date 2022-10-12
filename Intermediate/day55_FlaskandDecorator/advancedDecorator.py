class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


# When the function to decorate have inputs
# should use Advanced Decorator with *args and **kwargs
def is_authenticate_decorator(function):
    # function as an attribute have inputs [user]
    def wrapper(*args):
        # args[0]: the first input
        if args[0].is_logged_in:
            print(args)
            print(args[0], args[0].name, args[0].is_logged_in)
            function(args[0])
    return wrapper


@ is_authenticate_decorator
def create_blog_post(user):
    print(f"This id {user.name}'s new blog post")


blog_user = User("Jin")
blog_user.is_logged_in = True
create_blog_post(blog_user)
