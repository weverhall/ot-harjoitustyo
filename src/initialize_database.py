from database_connection import get_database_connection


def create_table(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY NOT NULL,
            host TEXT,
            address TEXT,
            ping TEXT,
            search_date DATE DEFAULT CURRENT_DATE,
            UNIQUE(host, search_date)
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    create_table(connection)


if __name__ == "__main__":
    initialize_database()
