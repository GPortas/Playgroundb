class Exercise:

    def __init__(self, _id=None, question=None, solution=None):
        self._id = _id
        self.question = question
        self.solution = solution

    def get_id(self):
        return self._id

    def get_question(self):
        return self.question

    def get_solution(self):
        return self.solution
