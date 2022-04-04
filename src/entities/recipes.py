import uuid

class Recipes:

    def __init__ (self, ingredients, howto, user=None, id=None):
        self.user = user
        self.ingredients = ingredients
        self.howto = howto
        self.id = id or str(uuid.uuid4())