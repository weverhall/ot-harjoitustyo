from database_connection import get_database_connection

def create_tables(connection):
    cur = connection.cursor()

<<<<<<< HEAD
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS domains (
            id INTEGER PRIMARY KEY,
            name TEXT

        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ips (
            name TEXT PRIMARY KEY,
            domain_id INTEGER REFERENCES domains
        );
    ''')
=======
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
>>>>>>> 4aaace358a7d0c2ff4fec776779a4620c9ff7304


    connection.commit()


def initialize_database():
    connection = get_database_connection()
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
