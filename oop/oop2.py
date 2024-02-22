class StarCookie:
    def __init__(self) -> None:
        print("The cookie is ready")


star_cookie1 = StarCookie()

star_cookie1.weight = 15
star_cookie1.height = 20
star_cookie1.color = "Red"

print(star_cookie1.weight)
print(star_cookie1.color)


star_cookie2 = StarCookie()

star_cookie2.weight = 1
star_cookie2.height = 2
star_cookie2.color = "Blue"

print(star_cookie2.weight)
print(star_cookie2.color)


class Youtube:
    def __init__(self, username, subscribers = 0) -> None:
        self.username = username
        self.subscribers = subscribers

user1 = Youtube("Elshad")

print(user1.username)
print(user1.subscribers)