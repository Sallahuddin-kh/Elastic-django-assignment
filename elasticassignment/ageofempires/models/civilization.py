from ageofempires.models.BaseModel import BaseModel

class Civilization(BaseModel):

    def get_index_name(self):
        """
        Gets the index_name according to model
        """
        return 'civilizations'
