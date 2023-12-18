
# class User:
#     pass
#
#
# user_one = User()
# user_one.id = "100"
# user_one.name = "Sunny"
#
# print(user_one.id)
# print(user_one.name)

# User class
class User:

    def __init__(self, user_id, user_name):
        """User constructor."""
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """User follows another user."""
        user.followers += 1
        self.following += 1


user_one = User("001", "Sunny")
user_two = User("002", "Jack")

print(user_one.id)
print(user_one.name)
print(user_one.followers)

user_one.follow(user_two)

print(user_one.following)
print(user_one.followers)
print(user_two.following)
print(user_two.followers)
