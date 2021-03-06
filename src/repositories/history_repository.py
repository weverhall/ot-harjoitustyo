from platform import system as platform_os
from database_connection import get_database_connection


class HistoryRepository:
    """Repository class responsible for database functionality

    Attributes:
        connection: database_connection method for acquiring database connection
    """

    def __init__(self, connection):
        self._connection = connection

    def fetch_all(self):
        """Fetches and sorts all data from database

        Returns:
            List-type object of fetched data
        """

        cursor = self._connection.cursor()

        cursor.execute('SELECT host, address, ping, search_date FROM history\
                        ORDER BY search_date DESC, host ASC')

        rows = cursor.fetchall()

        results = [list(row) for row in rows]

        return results

    def clear_all(self):
        """Removes all data from database"""

        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM history')

        self._connection.commit()

    def insert(self, host, address, ping):
        """Inserts output from NetworkLookup class to database

        Args:
            host (str): Domain search parameter
            address (str): Domain's address or name
            ping (str): Domain's ping
        """

        cursor = self._connection.cursor()

        full_ping = ping[9:-3]

        if ping[:7] == "Pinging":
            ping = "?"
        else:
            if platform_os().lower() != "windows":
                ping = full_ping
                ping = str(round(float(ping), 1)).rstrip("0") + " ms"
                if ping[0] == "0":
                    ping = full_ping.rstrip("0") + " ms"
                if ping.rstrip(" ms")[-1] == ".":
                    ping = ping.rstrip(" ms")
                    ping = ping.rstrip(".") + " ms"
            else:
                ping = ping[9:]

        cursor.execute(
            'INSERT OR REPLACE INTO history (host, address, ping) VALUES (?, ?, ?)',
            (host, address, ping))

        self._connection.commit()


history_repository = HistoryRepository(get_database_connection())
