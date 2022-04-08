from database_connection import get_database_connection
from repositories.recipes_repository import RecipesRepository

class RecipesService:

    def __init__ (self):
        self.recipes_repository = RecipesRepository(get_database_connection())

    def add_recipe (self, title, instructions):
        self.recipes_repository.add_recipe(title, instructions)