class CallHandler:
    """ A class that initializes call handlers
        and controls the call system.
    """
    def __init__(self, respondents, managers, directors):
        """ Input: lists of respondents based on levels
            Task: initialize variables
        """
        self.num_respondents = len(respondents)
        self.num_managers = len(managers)
        self.num_directors = len(directors)
        self.employees = []
        self.call_queues = []
        for i in [respondents, managers, directors]:
            self.employees.append(i)

    def get_call_handler(self, call):
        """ Input: call (Call) from a customer
            Return the Employee who handles the call
        """



