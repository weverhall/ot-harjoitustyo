from database_connection import get_database_connection


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recipes (
            id INTEGER PRIMARY KEY,
            title TEXT,
            instructions TEXT

        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ingredients (
            name TEXT PRIMARY KEY,
            recipe_id INTEGER REFERENCES Recipes
        );
    ''')


    connection.commit()


def initialize_database():
    connection = get_database_connection()

    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
