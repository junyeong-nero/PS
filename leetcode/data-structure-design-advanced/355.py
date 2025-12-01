class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = dict()
        self.follow_info = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque([])
        self.tweets[userId].appendleft((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news = list(self.tweets.get(userId, []))
        for other in self.follow_info.get(userId, []):
            news += self.tweets.get(other, [])
        news = sorted(news, reverse=True)[:10]
        return [tweetId for time, tweetId in news]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_info:
            self.follow_info[followerId] = set()
        self.follow_info[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_info:
            return
        self.follow_info[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
