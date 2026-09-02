class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId][:]
        for followee in self.following[userId]:
            feed.extend(self.tweets[followee])
        heapq.heapify(feed)

        most_recent = []
        counter = 0
        while feed and counter < 10:
            most_recent.append(heapq.heappop(feed)[1])
            counter += 1
        
        return most_recent

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)