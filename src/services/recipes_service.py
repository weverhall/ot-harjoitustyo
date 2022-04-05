from database_connection import get_database_connection
from repositories.recipes_repository import RecipesRepository

class RecipesService:

    def __init__ (self):
        self.recipes_repository = RecipesRepository(get_database_connection())

    #def create(self, title, ingredients):