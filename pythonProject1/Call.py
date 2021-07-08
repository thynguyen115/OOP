import HandlerRank


##################################
#       Call's conversation      #
##################################
def reply_message():
    print("Hello, how can I help you?")


def end_call():
    print("Thank you for calling")


class Call:
    """ A class that holds info of caller and call handler """

    def __init__(self, caller):
        """ Initialize caller, handler, handler's rank """
        self.caller = caller
        self.handler = None
        self.handler_rank = HandlerRank.respondent.value

    ##################################
    #       Handler's Info           #
    ##################################
    def set_handler(self, employee):
        """ set handler """
        self.handler = employee

    def get_handler(self):
        """ get handler """
        return self.handler

    def set_handler_rank(self, new_rank):
        """ set new rank for handler """
        self.handler_rank = new_rank

    def get_handler_rank(self):
        """ get handler rank """
        return self.handler_rank

    def increment_rank(self):
        """ Increase the level of handler by 1 """
        if self.handler_rank == 1:
            self.handler_rank = HandlerRank.manager.value
        elif self.handler_rank == 2:
            self.handler_rank = HandlerRank.director.value
        else:
            self.handler_rank = None  # cannot increment anymore
        return self.handler_rank
