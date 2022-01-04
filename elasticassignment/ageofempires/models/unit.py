from ageofempires.models.BaseModel import BaseModel

class Unit(BaseModel):

    def get_index_name(self):
        """
        Gets the index_name according to model
        """
        return 'units'
