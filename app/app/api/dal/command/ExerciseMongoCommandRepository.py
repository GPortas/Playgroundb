from app.api.dal.PdbMongoBaseRepository import PdbMongoBaseRepository
from app.api.dal.command.errors.CommandError import CommandError
from app.api.services.dalinterfaces.command.IExerciseCommandRepository import IExerciseCommandRepository
from app.configuration import settings


class ExerciseMongoCommandRepository(IExerciseCommandRepository, PdbMongoBaseRepository):

    def __init__(self):
        super(ExerciseMongoCommandRepository, self).__init__(
            connection_uri=settings.PDB_MONGO_CONNECTION_PROPS['CONNECTION_URI'],
            dbname=settings.PDB_MONGO_CONNECTION_PROPS['DBNAME'])

    def create_exercise(self, exercise):
        try:
            self.db.exercises.insert_one(exercise.to_json_dict())
        except Exception as qe:
            raise CommandError(str(qe))
