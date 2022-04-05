import uuid

class Recipes:

    def __init__ (self, ingredients, howto, id=None):
        self.ingredients = ingredients
        self.howto = howto
        self.id = id or str(uuid.uuid4())