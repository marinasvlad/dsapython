class Youtube:
    def __init__(self,username, subscribers = 0) -> None:
        self.username = username
        self.subscribers = subscribers

    def subscribe(self, user):
        user.subscribers += 1

user1 = Youtube("Elshad")
user2 = Youtube("Renad")

print(user1.subscribers)
print(user2.subscribers)
