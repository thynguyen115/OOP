import enum


class HandlerRank(enum.Enum):
    respondent = 1
    manager = 2
    director = 3

    def __init__(self, r):
        self.rank = r

    def get_rank(self):
        return self.rank


respondent = HandlerRank.respondent
manager = HandlerRank.manager
director = HandlerRank.director
