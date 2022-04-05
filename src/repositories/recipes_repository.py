import sqlite3

class RecipesRepository:
    def __init__ (self, connection):
        self.connection = connection
        self.cur = self.connection.cursor()

    def add_recipe(self, title, instructions):
        self.cur.execute
        ('INSERT INTO Recipes(title, instructions) VALUES (:title, :instructions)', 
        {'title':title, 'instructions':instructions})

        self.connection.commit()