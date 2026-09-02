class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:
            if self.tweets[followee]:
                i = len(self.tweets[followee]) - 1
                time, tweet = self.tweets[followee][i]
                heap.append((time, tweet, followee, i - 1))

        heapq.heapify(heap)

        most_recent = []
        while heap and len(most_recent) < 10:
            time, tweet, followee, i = heapq.heappop(heap)
            most_recent.append(tweet)

            if i >= 0:
                time, tweet = self.tweets[followee][i]
                heapq.heappush(heap, (time, tweet, followee, i - 1))
        
        return most_recent

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)