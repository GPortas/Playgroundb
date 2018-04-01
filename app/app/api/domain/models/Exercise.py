from app.api.domain.models.BaseModel import BaseModel


class Exercise(BaseModel):

    def __init__(self, author, collection_name, collection_data, question, solution, _id=None):
        self.author = author
        self.collection_name = collection_name
        self.collection_data = collection_data
        if _id is not None:
            self._id = _id
        self.question = question
        self.solution = solution

    def get_id(self):
        return self._id

    def get_question(self):
        return self.question

    def get_solution(self):
        return self.solution

    def get_author(self):
        return self.author

    @staticmethod
    def from_json(json_source):
        exercise = Exercise(author=json_source["author"], collection_name=json_source["collection_name"],
                            collection_data=json_source["collection_data"], _id=json_source.get("_id"),
                            question=json_source["question"], solution=json_source["solution"])
        return exercise
