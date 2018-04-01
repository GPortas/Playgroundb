from app.api.domain.models.BaseModel import BaseModel


class Exercise(BaseModel):

    def __init__(self, author, collection_name, question, solution, collection_data=None, _id=None):
        self.author = author
        self.collection_name = collection_name
        if collection_data is not None:
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

    def set_collection_data(self, data):
        self.collection_data = data

    def get_collection_data(self):
        return self.collection_data

    def get_collection_name(self):
        return self.collection_name

    @staticmethod
    def from_json(json_source):
        exercise = Exercise(author=json_source["author"], collection_name=json_source["collection_name"]
                            , _id=json_source.get("_id"), question=json_source["question"],
                            solution=json_source["solution"], collection_data=json_source.get("collection_data", None))
        return exercise
