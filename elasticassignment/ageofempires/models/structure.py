from ageofempires.models.BaseModel import BaseModel

class Structure(BaseModel):

    def get_index_name(self):
        """
        Gets the index_name according to model
        """
        return 'structures'
