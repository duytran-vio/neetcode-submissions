class User:
    def __init__(self):
        self.tweets = []
        self.followed = {}
        self.mostRecentTweets = []

    def addNewTweet(self, tweedId: int):
        self.tweets.append(tweedId)

    def followUser(self, userId: int):
        self.followed[userId] = True

    def unFollowUser(self, userId: int):
        self.followed[userId] = False

class Twitter:

    def __init__(self):
        self.users = {}

    def getUserByUserId(self, userId: int) -> User:
        if userId not in self.users:
            self.users[userId] = User()
        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.getUserByUserId(userId)
        user.addNewTweet(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.getUserByUserId(userId)
        mostRecentFeed = []
        for followedUserId, isFollow in user.followed.items():
            if not isFollow: continue
            followedUser = self.getUserByUserId(followedUserId)
            if len(followedUser.tweets) > 0:
                heapq.heappush(mostRecentFeed, (-followedUser.tweets[-1], followedUser, len(followedUser.tweets) - 1))

        if len(user.tweets) > 0:
            heapq.heappush(mostRecentFeed, (-user.tweets[-1], user, len(user.tweets) - 1))

        k = 0
        res = []
        while mostRecentFeed and k < 10:
            invert_tweet_id, owner, tweet_index = heapq.heappop(mostRecentFeed)
            res.append(-invert_tweet_id)
            tweet_index -= 1
            if (tweet_index >= 0):
                heapq.heappush(mostRecentFeed, (-owner.tweets[tweet_index], owner, tweet_index))
            k += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        followerUser = self.getUserByUserId(followerId)
        followerUser.followUser(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        followerUser = self.getUserByUserId(followerId)
        followerUser.unFollowUser(followeeId)
        