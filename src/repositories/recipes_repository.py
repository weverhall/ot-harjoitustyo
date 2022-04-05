import sqlite3

class RecipesRepository:
    def __init__ (self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def fetch_recipes(self):
        self.cursor.execute('SELECT * FROM Recipes')

        return self.cursor.fetchall()

    def fetch_ingredients(self):
        self.cursor.execute('SELECT * FROM Ingredients')

        return self.cursor.fetchall()
