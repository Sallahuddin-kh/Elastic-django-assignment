from ageofempires.models.BaseModel import BaseModel

class Technology(BaseModel):

    def set_index_name(self):
        """
        Sets an the index_name instance variable to model value
        """
        self.index_name = 'technologies'

    def __init__(self):
        """
        Constructor calls the parent constructor and then set_index_method
        """
        super().__init__()
        self.set_index_name()
