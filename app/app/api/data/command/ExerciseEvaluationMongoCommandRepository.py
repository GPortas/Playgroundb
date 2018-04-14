from app.api.data.PdbMongoBaseRepository import PdbMongoBaseRepository
from app.api.domain.models.ExerciseEvaluation import ExerciseEvaluation
from app.api.domain.services.data.command.IExerciseEvaluationCommandRepository import \
    IExerciseEvaluationCommandRepository
from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.configuration import settings


class ExerciseEvaluationMongoCommandRepository(IExerciseEvaluationCommandRepository, PdbMongoBaseRepository):

    def __init__(self):
        super(ExerciseEvaluationMongoCommandRepository, self).__init__(
            connection_uri=settings.PDB_MONGO_CONNECTION_PROPS['CONNECTION_URI'],
            db_name=settings.PDB_MONGO_CONNECTION_PROPS['DBNAME'])

    def create_exercise_evaluation(self, exercise_evaluation):
        try:
            self.db.evaluations.insert_one(exercise_evaluation.to_json_dict())
        except Exception as qe:
            raise CommandError(str(qe))

    def increment_exercise_evaluation_attempts(self, exercise_evaluation):
        try:
            self.db.evaluations.update({'_id': exercise_evaluation.get_id()},
                                       {'$set': {'attempt': exercise_evaluation.get_attempt() + 1}})
        except Exception as qe:
            raise CommandError(str(qe))

    def update_exercise_evaluation_as_solved(self, exercise_evaluation, score):
        try:
            self.db.evaluations.update({'_id': exercise_evaluation.get_id()},
                                       {'$set': {'score': score,
                                                 'status': ExerciseEvaluation.STATUS_SOLVED}})
        except Exception as qe:
            raise CommandError(str(qe))
