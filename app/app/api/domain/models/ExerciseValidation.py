from app.api.domain.models.BaseModel import BaseModel


class ExerciseValidation(BaseModel):

    def __init__(self, is_correct):
        self.is_correct = is_correct
