from sqlite3 import connect

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file.

    :param db_file: Path to the database file
    :return: Connection object or None if an error occurs
    """
    try:
        conn = connect(db_file)
        return conn
    except Exception as e:
        print(f'Error connecting to {db_file}: {e}')
        return None