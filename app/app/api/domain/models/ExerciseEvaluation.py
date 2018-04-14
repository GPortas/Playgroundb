from bson import ObjectId

from app.api.domain.models.BaseModel import BaseModel


class ExerciseEvaluation(BaseModel):
    STATUS_UNSOLVED = 'unsolved'
    STATUS_SOLVED = 'solved'

    def __init__(self, user_id, exercise_id, _id=None, status=None, attempt=None, score=None):
        self.user_id = user_id
        self.exercise_id = exercise_id
        if _id is not None:
            self._id = _id
        if status is not None:
            self.status = status
        else:
            self.status = self.STATUS_UNSOLVED
        if attempt is not None:
            self.attempt = attempt
        else:
            self.attempt = 1
        if score is not None:
            self.score = score
        else:
            self.score = 0

    def get_id(self):
        return self._id

    def get_attempt(self):
        return self.attempt

    def get_score(self):
        return self.score

    def get_status(self):
        return self.status

    @staticmethod
    def from_json(json_source):
        exercise = ExerciseEvaluation(user_id=json_source["user_id"], exercise_id=json_source["exercise_id"]
                                      , _id=json_source.get("_id"), status=json_source.get("status"),
                                      attempt=json_source.get("attempt"),
                                      score=json_source.get("score"))
        return exercise

    def to_json_dict(self):
        result = super(ExerciseEvaluation, self).to_json_dict()
        result["user_id"] = ObjectId(result.get("user_id"))
        result["exercise_id"] = ObjectId(result.get("exercise_id"))
        return result
