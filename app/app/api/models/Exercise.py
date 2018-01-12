class Exercise:

    def __init__(self, author, _id=None, question=None, solution=None):
        self._id = _id
        self.question = question
        self.solution = solution
        self.author = author

    def get_id(self):
        return self._id

    def get_question(self):
        return self.question

    def get_solution(self):
        return self.solution

    def get_author(self):
        return self.author

    def validate_answer(self, answer):
        return self.solution == answer
