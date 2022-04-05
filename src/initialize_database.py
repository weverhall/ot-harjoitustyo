from database_connection import get_database_connection

def create_tables(connection):
    cur = connection.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Recipes (
            id INTEGER PRIMARY KEY NOT NULL,
            title TEXT,
            instructions TEXT
        );
    ''')

    #cur.execute('''
    #    CREATE TABLE IF NOT EXISTS Ingredients (
    #        name TEXT PRIMARY KEY,
    #        recipe_id INTEGER REFERENCES Recipes(id)
    #    );
    #''')


    connection.commit()


def initialize_database():
    connection = get_database_connection()
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
