from app.api.models.BaseModel import BaseModel


class Exercise(BaseModel):

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

    @staticmethod
    def from_json(json_source):
        exercise = Exercise(author=json_source["author"], _id=json_source.get("_id"),
                            question=json_source["question"],
                            solution=json_source["solution"])
        return exercise
