from bson import ObjectId

from app.api.data.PdbMongoBaseRepository import PdbMongoBaseRepository
from app.api.domain.models.ExerciseEvaluation import ExerciseEvaluation
from app.api.domain.services.data.query.IExerciseEvaluationQueryRepository import IExerciseEvaluationQueryRepository
from app.configuration import settings


class ExerciseEvaluationMongoQueryRepository(IExerciseEvaluationQueryRepository, PdbMongoBaseRepository):
    ITEM_REQUIRED_FIELDS = {'_id': 1, 'user_id': 1, 'exercise_id': 1, 'status': 1, 'attempt': 1, 'score': 1}

    def __init__(self):
        super(ExerciseEvaluationMongoQueryRepository, self).__init__(
            connection_uri=settings.PDB_MONGO_CONNECTION_PROPS['CONNECTION_URI'],
            db_name=settings.PDB_MONGO_CONNECTION_PROPS['DBNAME'])

    def get_exercise_evaluation(self, user_id, exercise_id):
        query_result = self.db.evaluations.find_one(
            {'user_id': ObjectId(user_id), 'exercise_id': ObjectId(exercise_id)},
            self.ITEM_REQUIRED_FIELDS)
        if query_result is not None:
            exercise = ExerciseEvaluation.from_json(query_result)
            return exercise
        else:
            return None
