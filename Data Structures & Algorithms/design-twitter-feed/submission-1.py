class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        count = 0
        for i in range(len(self.tweets)-1,-1,-1):
            tweetId = self.tweets[i][0]
            tweet_userId = self.tweets[i][1]

            if count < 10 and (tweet_userId == userId or tweet_userId in self.following[userId]):
                feed.append(tweetId)
                count += 1

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)