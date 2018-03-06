from app.api.domain.models.BaseModel import BaseModel


class QueryExecution(BaseModel):

    def __init__(self, execution_result):
        self.execution_result = execution_result
