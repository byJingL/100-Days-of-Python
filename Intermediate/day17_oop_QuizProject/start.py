class User:
    # Constructor / Initialize
    # Initial function: when construct a new object from this class
    # initialize the attributes / create the start values of attributes
    # Everytime construct from this class, this init function will be triggered
    # must provide this start data
    # more convenient: parameter: user_id == attribute: id
    def __init__(self, user_id, username):
        print("a new user will be created...")
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    # Self parameter must be the first parameter
    # when this method is called, it knows the object call it
    # you'll never see self when you're using objects
    # :but you see it a lot when you're writing your code inside your class
    def follow(self, user):
        user.follower += 1
        self.following += 1


# user_1: Object
user_1 = User("001", "Jenny")
user_2 = User("002", "Mian")

user_1.follow(user_2)

# id, username: Attribute
print(f"user1: {user_1.id}, follower: {user_1.follower}, following: {user_1.following}")
print(f"user2: {user_2.id}, follower: {user_2.follower}, following: {user_2.following}")

