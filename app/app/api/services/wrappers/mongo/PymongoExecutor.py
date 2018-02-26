class PymongoExecutor:

    def __init__(self, db):
        self.__db = db

    def execute(self, expression):
        return eval(expression)
