from bson import ObjectId

from app.api.data.PdbMongoBaseRepository import PdbMongoBaseRepository
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.domain.models.Exercise import Exercise
from app.api.domain.services.data.query.IExerciseQueryRepository import IExerciseQueryRepository
from app.configuration import settings


class ExerciseMongoQueryRepository(IExerciseQueryRepository, PdbMongoBaseRepository):
    ITEM_PROJECTION = {'$project': {
        '_id': 1,
        'question': 1,
        'solution': 1,
        'author': 1,
        'collection_name': 1,
        'collection_data': 1
    }}

    def __init__(self):
        super(ExerciseMongoQueryRepository, self).__init__(
            connection_uri=settings.PDB_MONGO_CONNECTION_PROPS['CONNECTION_URI'],
            db_name=settings.PDB_MONGO_CONNECTION_PROPS['DBNAME'])

    def get_exercise_by_id(self, exercise_id):
        pipeline = [
            {'$match': {'_id': ObjectId(exercise_id)}},
            self.ITEM_PROJECTION
        ]
        result = self.db.exercises.aggregate(pipeline=pipeline)

        n_elements = 0

        for item in result:
            n_elements += 1
            return Exercise.from_json(item)

        if n_elements == 0:
            raise ResourceNotFoundQueryError("Exercise with id" + exercise_id + " not found")

    def get_all_exercises(self):
        result = self.db.exercises.find({})
        return_result = []
        for doc in result:
            return_result.append(Exercise.from_json(doc))
        return return_result
