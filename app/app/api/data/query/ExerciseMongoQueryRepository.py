from bson import ObjectId

from app.api.data.PdbMongoBaseRepository import PdbMongoBaseRepository
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.domain.models.Exercise import Exercise
from app.api.domain.services.data.query.IExerciseQueryRepository import IExerciseQueryRepository
from app.configuration import settings


class ExerciseMongoQueryRepository(IExerciseQueryRepository, PdbMongoBaseRepository):
    ITEM_REQUIRED_FIELDS = {'_id': 1,
                            'question': 1,
                            'solution': 1,
                            'author': 1,
                            'collection_name': 1,
                            'collection_data': 1,
                            'time': 1}

    ITEM_LIST_RETURNED_LIMIT = 20

    def __init__(self):
        super(ExerciseMongoQueryRepository, self).__init__(
            connection_uri=settings.PDB_MONGO_CONNECTION_PROPS['CONNECTION_URI'],
            db_name=settings.PDB_MONGO_CONNECTION_PROPS['DBNAME'])

    def get_exercise_by_id(self, exercise_id):
        query_result = self.db.exercises.find_one({'_id': ObjectId(exercise_id)}, self.ITEM_REQUIRED_FIELDS)
        if query_result is None:
            raise ResourceNotFoundQueryError('Exercise with id ' + exercise_id + ' not found')
        else:
            return Exercise.from_json(query_result)

    def get_exercises_list(self, limit=ITEM_LIST_RETURNED_LIMIT):
        result = self.db.exercises.find({}).limit(limit)
        return_result = []
        for doc in result:
            return_result.append(Exercise.from_json(doc))
        return return_result
