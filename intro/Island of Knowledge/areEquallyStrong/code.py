def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    you = []
    friend = []

    you.append(yourLeft)
    you.append(yourRight)
    friend.append(friendsLeft)
    friend.append(friendsRight)

    return sorted(you) == sorted(friend)
