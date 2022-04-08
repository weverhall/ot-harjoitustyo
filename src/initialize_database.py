from database_connection import get_database_connection

def create_tables(connection):
    cursor = connection.cursor()

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

    connection.commit()

def initialize_database():
    connection = get_database_connection()
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
