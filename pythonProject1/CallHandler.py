from Call import Call


class CallHandler:
    """ A class that initializes a list of call handlers based on their levels
        and controls the call system. It will assign the handler or save the
        calls into a queue when nobody is available
    """
    def __init__(self, respondents, managers, directors):
        """ Input: lists of respondents based on levels
            Task: initialize variables
            Note: employee_levels[0] = list of respondents
                  employee_levels[1] = list of managers
                  employee_levels[-1] = list of directors
        """
        self.num_respondents = len(respondents)
        self.num_managers = len(managers)
        self.num_directors = len(directors)
        self.num_people_per_level = [self.num_respondents,
                                     self.num_managers, self.num_directors]
        self.employee_levels = []
        self.call_queues = []
        for i in [respondents, managers, directors]:
            self.employee_levels.append(i)

    def get_call_handler(self, call):
        """ Input: call (Call) from a customer
            Return the Employee who handles the call
        """
        for level in self.employee_levels:
            for emp in level:
                # Find the first available employee
                if emp.isAvailable():
                    return emp
        return None

    def dispatch_call(self, caller):
        """ Assign the call to a free employee
            Or save the call in a queue if no one is available
        """
        call = Call(caller)
        emp = self.get_call_handler(call)
        curr_rank = call.get_handler_rank()
        if emp is None:
            if len(self.call_queues[curr_rank]) == \
                    self.num_people_per_level[curr_rank]:
                curr_rank += 1  # Assume curr_rank does not exceed director rank
            else:
                self.call_queues[curr_rank] += [call]
            call.reply_message()
        else:
            call.set_handler(emp)
            emp.receive_call(call)
