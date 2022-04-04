from entities.recipes import Recipes
from entities.user import User

class RecipesService:

    def __init__ (self, placeholderRepos):
        self._user = None
        self.placeholderRepos

    def create_recipe(self, ingredients, howto):
        recipe = Recipes(ingredients = ingredients, 
        howto = howto, 
        user = self._user)

        return self._repoPlaceholder.create(recipe)


    def login(self, username, password):
        user = self._placeholderRepo...

        return user

    def create_user(self, username, password):
        