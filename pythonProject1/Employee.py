# import CallHandler, Call
from HandlerRank import HandlerRank


class Employee:
    def __init__(self, rank):
        self.rank = rank
        self.call = None

    def receive_call(self, call):
        """ employee receives the call
            the call gets info about employee and his/her rank
        """
        self.call = call
        call.set_handler(self)
        call.set_handler_rank(self.rank)

    def call_completed(self):
        """ employee becomes available since call is now None """
        self.call = None

    def is_available(self):
        """ Available when currently having no call """
        return self.call is None

    def get_rank(self):
        return self.rank


class Respondent(Employee):
    def __init__(self):
        self.rank = HandlerRank.respondent.value
        super().__init__(self.rank)


class Manager(Employee):
    def __init__(self):
        self.rank = HandlerRank.manager.value
        super().__init__(self.rank)


class Director(Employee):
    def __init__(self):
        self.rank = HandlerRank.respondent.value
        super().__init__(self.rank)
