from database_connection import get_database_connection


class HistoryRepository:
    def __init__(self, connection):
        self._connection = connection

    def fetch_all(self):
        cursor = self._connection.cursor()

        cursor.execute('SELECT host, address, ping, search_date FROM history\
                        ORDER BY search_date DESC, host ASC\
                        LIMIT 150')

        rows = cursor.fetchall()

        results = [list(row) for row in rows]

        return results

    def clear_all(self):
        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM history')

        self._connection.commit()

    def insert(self, host, address, ping):
        cursor = self._connection.cursor()

        if ping[:7] != "Pinging":
            ping = ping[9:-3]
        else:
            ping = "?"

        cursor.execute(
            'INSERT OR IGNORE INTO history (host, address, ping) VALUES (?, ?, ?)',
            (host, address, ping))

        self._connection.commit()


history_repository = HistoryRepository(get_database_connection())
