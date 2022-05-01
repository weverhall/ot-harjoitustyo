from database_connection import get_database_connection


class HistoryRepository:
    def __init__(self, connection):
        self._connection = connection

    def fetch_all(self):
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM history')

        rows = cursor.fetchall()

        return rows

    def clear_all(self):
        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM history')

        self._connection.commit()

    def insert(self, host, address, ping):
        cursor = self._connection.cursor()
        
        ping = ping[9:-3]

        cursor.execute(
            'INSERT INTO history (host, address, ping) VALUES (?, ?, ?)', 
            (host, address, ping))

        self._connection.commit()

history_repository = HistoryRepository(get_database_connection())
