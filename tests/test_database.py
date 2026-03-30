from src.atlasdoc_storage_data_v1.database import create_connection

def test_create_connection():
    db_file = 'test.db'
    connection = create_connection(db_file)
    assert connection is not None