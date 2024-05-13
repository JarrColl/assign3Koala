import json
import os


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.DATABASE_FILE_DIRECTORY = "./Database"

        # Check if 'database' directory exists.
        if not os.path.exists(self.DATABASE_FILE_DIRECTORY):
            os.makedirs(self.DATABASE_FILE_DIRECTORY)
            print("Created a the database directory.")

    def _getFile(self, name: str, mode: str):
        file_path = self.DATABASE_FILE_DIRECTORY + "/" + name + ".json"
        # Check if the file exists, if it doesn't then create it.
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write("[]")
        return open(file_path, mode)

    def getTableData(self, name: str):
        return json.load(self._getFile(name, "r"))

    def writeTableData(self, name: str, data: list):
        file_path = self.DATABASE_FILE_DIRECTORY + "/" + name + ".json"
        with open(file_path, "w") as file:
            json.dump(data, file)
